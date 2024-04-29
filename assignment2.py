class CacheBlock:
    def __init__(self, tag=None, data=None, last_used=0, dirty_bit=False):
        self.tag = tag
        self.data = data
        self.last_used = last_used
        self.dirty_bit = dirty_bit

def calculate_bits(memory_size, cache_size, block_size):
    total_bits = memory_size.bit_length()
    offset_bits = block_size.bit_length()
    tag_bits = total_bits - offset_bits
    return total_bits, tag_bits, offset_bits

def main():
    memory_size = int(input("Enter main memory size (in bytes): "))
    cache_size = int(input("Enter cache size (in bytes): "))
    block_size = int(input("Enter block size (in bytes): "))

    total_bits, tag_bits, offset_bits = calculate_bits(memory_size, cache_size, block_size)
    print(f"Total bits: {total_bits}, Tag bits: {tag_bits}, Offset bits: {offset_bits}")

    cache_blocks = [CacheBlock() for _ in range(cache_size // block_size)]
    memory_blocks = [i for i in range(memory_size // block_size)]

    while True:
        address = int(input("Enter memory address (or -1 to exit): "))
        if address == -1:
            break
        
        block_offset = address % block_size
        tag = address // block_size

        write_policy = input("Choose write policy (write-through or write-back): ").lower()

        if any(block.tag == tag for block in cache_blocks if block.tag is not None):
            print("Cache hit!")
            cache_blocks[next(idx for idx, block in enumerate(cache_blocks) if block.tag == tag and block.tag is not None)].last_used = 0
            if write_policy == 'write-back':
                idx = next(idx for idx, block in enumerate(cache_blocks) if block.tag == tag and block.tag is not None)
                cache_blocks[idx].dirty_bit = True
        else:
            print("Cache miss!")
            empty_block = next((block for block in cache_blocks if block.tag is None), None)
            if empty_block is not None:
                print(f"Adding block with tag {tag} to cache")
                empty_block.tag = tag
                empty_block.data = memory_blocks[address // block_size]
                empty_block.last_used = 0
                if write_policy == 'write-back':
                    empty_block.dirty_bit = True
            else:
                print("Cache is full. Performing LRU replacement.")

                # Find the block with the highest last_used value (LRU block)
                lru_block_index = max(range(len(cache_blocks)), key=lambda i: cache_blocks[i].last_used)
                lru_block = cache_blocks[lru_block_index]
                print(f"Replacing block with tag {lru_block.tag}")
                lru_block.tag = tag
                lru_block.data = memory_blocks[address // block_size]
                lru_block.last_used = 0
                lru_block.dirty_bit = False  # Clear dirty bit for LRU replacement

                if write_policy == 'write-back':
                    lru_block.dirty_bit = True

        for block in cache_blocks:
            block.last_used += 1

        print("Cache state after operation:")
        for idx, block in enumerate(cache_blocks):
            tag_binary = bin(block.tag)[2:].zfill(tag_bits) if block.tag is not None else 'None'
            data_binary = bin(block.data)[2:].zfill(block_size.bit_length()) if block.data is not None else 'None'
            dirty_status = 'Dirty' if block.dirty_bit else 'Clean'
            print(f"Block {idx}: Tag={tag_binary}, Data={data_binary}, Last Used={block.last_used}, {dirty_status}")

if __name__ == "__main__":
    main()
