"""
Utility: deletes student.db so you can rehearse a section from a clean slate.
Not part of the presentation itself.
"""

import os

if os.path.exists("student.db"):
    os.remove("student.db")
    print("Deleted student.db")
else:
    print("student.db does not exist, nothing to delete")
