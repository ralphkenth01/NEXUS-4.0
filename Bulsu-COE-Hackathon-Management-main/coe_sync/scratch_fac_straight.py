import sqlite3

c = sqlite3.connect("instance/coe_sync.db")
n = c.execute("UPDATE faculty SET preferred_session_type='STRAIGHT'").rowcount
c.commit()
print("updated", n)
