import asyncio
import aiohttp
import logging
import time
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AsyncTelemetryPoller:
    """Asynchronous telemetry daemon for multi-vendor network devices."""
    
    def __init__(self, targets: List[Dict[str, Any]], max_concurrency: int = 50):
        self.targets = targets
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.session = None

    async def poll_device(self, target: Dict[str, Any]) -> Dict[str, Any]:
        """Polls single network device RESTCONF interface with async semaphore rate-limiting."""
        async with self.semaphore:
            url = f"https://{target['ip']}/restconf/data/ietf-interfaces:interfaces-state"
            headers = {"Accept": "application/yang-data+json"}
            
            start_time = time.time()
            try:
                async with self.session.get(url, headers=headers, timeout=5, ssl=False) as resp:
                    latency = (time.time() - start_time) * 1000
                    if resp.status == 200:
                        data = await resp.json()
                        return {
                            "host": target["hostname"],
                            "status": "SUCCESS",
                            "latency_ms": round(latency, 2),
                            "payload": data
                        }
                    return {"host": target["hostname"], "status": f"HTTP_{resp.status}"}
            except Exception as err:
                return {"host": target["hostname"], "status": "ERROR", "error": str(err)}

    async def run(self):
        """Spawns asyncio task gathering loop."""
        async with aiohttp.ClientSession() as session:
            self.session = session
            tasks = [self.poll_device(t) for t in self.targets]
            results = await asyncio.gather(*tasks)
            logging.info(f"Successfully polled {len(results)} target devices.")
            return results

if __name__ == "__main__":
    inventory = [{"hostname": f"router-0{i}", "ip": f"10.0.0.{i}"} for i in range(1, 101)]
    poller = AsyncTelemetryPoller(inventory, max_concurrency=20)
    asyncio.run(poller.run())
