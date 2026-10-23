import sys, time, subprocess
from collections import Counter

seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 30
codes = Counter()
end = time.monotonic() + seconds
while time.monotonic() < end:
    result = subprocess.run(['curl', '-sS', '--max-time', '3', '--cacert', '.secrets/server.crt', '--connect-to', 'counter.localtest.me:443:127.0.0.1:8443', '-o', '/dev/null', '-w', '%{http_code}', 'https://counter.localtest.me/api/counter'], capture_output=True, text=True)
    codes[result.stdout or '000'] += 1
    time.sleep(0.2)
print('HTTP responses:', dict(codes))
if set(codes) != {'200'}:
    sys.exit(1)
