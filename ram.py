import psutil

# Get the virtual memory details
memory_info = psutil.virtual_memory()

# Print total, available, used memory and memory percentage
print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
print(f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB")
print(f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
print(f"Memory Percentage: {memory_info.percent}%")
