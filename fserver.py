#!/usr/bin/env python3
import re
import sys
from fsocks import server, tunnel_server


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(tunnel_server.main())
