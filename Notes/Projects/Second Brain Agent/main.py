# main.py
import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path

# TODO: Import agents once created
# from src.orchestrator import SecondBrainOrchestrator

async def main():
    """Entry point for Second Brain Maintenance Agent Team"""
    load_dotenv()

    vault_root = os.getenv("VAULT_ROOT", ".")
    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"

    print(f"Starting Second Brain Agent...")
    print(f"Vault: {vault_root}")
    print(f"Dry run: {dry_run}")

    # TODO: Initialize and run orchestrator
    # orchestrator = SecondBrainOrchestrator(vault_root)
    # await orchestrator.run_daily_check()

    print("Architecture setup complete. Ready for agent implementation.")

if __name__ == "__main__":
    asyncio.run(main())
