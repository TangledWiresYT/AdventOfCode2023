total = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        nums = []
        for char in line:
            if char.isnumeric():
                nums.append(int(char))
        total += int(str(nums[0]) + str(nums[len(nums)-1]))
        print(total)

print(f"Final total: {total}")