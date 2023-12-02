import threading

# Create a reentrant lock that can be used across multiple threads
shared_lock = threading.RLock()
