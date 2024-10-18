This project is a Python-based simulation of a simple cache memory system. The simulation models a direct-mapped cache where memory blocks are stored in cache blocks. It supports two write policies: write-through and write-back. The cache uses Least Recently Used (LRU) replacement when it's full, replacing the least recently used block with a new memory block.

## Features
Cache and Memory Simulation: Models main memory and cache using memory blocks and cache blocks.
Write Policies: Supports both write-through and write-back cache writing policies.
LRU Replacement Policy: When the cache is full, it replaces the least recently used cache block.
Tag and Offset Calculation: Calculates tag and offset bits for the cache system based on memory size, cache size, and block size.
## How It Works
The user provides the main memory size, cache size, and block size as inputs.
The program calculates:
Total bits: The total number of bits required to represent memory addresses.
Tag bits: The bits used to identify which memory block a cache block contains.
Offset bits: The bits used to represent the offset within a block.
The program initializes cache and memory blocks.
The user provides memory addresses to access:
If the memory block is in the cache (cache hit), the cache block is updated.
If the memory block is not in the cache (cache miss), the block is fetched from memory and loaded into cache.
If the cache is full, the Least Recently Used (LRU) replacement policy replaces the least recently used block.
The user can choose between write-through and write-back policies:
Write-through: Updates both cache and main memory on each write.
Write-back: Updates only the cache; the memory is updated later when the block is replaced, indicated by the dirty bit.
