"""Example task that writes output to persistent storage on Spider.

Inside an Apptainer container the filesystem is read-only, so results must be
written to the host filesystem.  Pixitainer sets the ``INIT_CWD`` environment
variable to the directory from which ``apptainer run`` was invoked, which lives
on Spider's persistent storage.
"""

import os
from datetime import datetime, timezone
from pathlib import Path

output_dir = Path("output") # volume mount
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "hello.txt"
output_file.write_text(
    f"Hello from spider-pixi-template!\n"
    f"Ran at: {datetime.now(timezone.utc).isoformat()}\n"
)

print(f"Wrote output to {output_file}")
