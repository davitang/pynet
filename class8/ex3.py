from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from jnpr_devices import srx2

device = Device(**srx2)
device.open()
device.timeout = 60

cfg = Config(device)
#Ensure config lock
try:
    cfg.lock()
    print("Lock aquired!")
except LockError:
    print("Config is already locked!")

#send a command
cfg.load("set system host-name packet4life", format="set", merge=True)

#check diff
print("checking diff:\n")
print(cfg.diff())
print()

#cfg rollback
cfg.rollback(0)
print("config rolled back!\n")

#check diff
print("checking diff:\n")
print(cfg.diff())
print()

#unlock config mode
cfg.unlock()
