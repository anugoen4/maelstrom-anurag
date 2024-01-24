#!/usr/bin/env python3
import uuid, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Node.node import Node, Request, Body


async def generate(node: Node, req: Request) -> Body:
    new_id = str(uuid.uuid4())
    return {"type": "generate_ok", "id": f"{node.node_id}-{new_id}"}


if __name__ == "__main__":
    n = Node()
    n.on("generate", generate)
    n.run()
