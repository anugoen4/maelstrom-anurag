#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Node.node import Node, Request, Body


async def echo(node: Node, req: Request) -> Body:
    return {"type": "echo_ok", "echo": req.body["echo"]}


if __name__ == "__main__":
    n = Node()
    n.on("echo", echo)
    n.run()
