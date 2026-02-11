# caden and trent
import sys
import time

matrix: list[list[str | int]] = []
kp_files = []
all_items_gathered: list[list[int]] = []
time_start = 0.0
deadline_time = 0.0
timed_out = False


def read_file(kp_file: str):
    global matrix
    with open(kp_file, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(", ")
                parts_no_space = line.split(",")
                if (len(parts) != 2):
                    parts = parts_no_space
                if len(parts) == 2:
                    matrix.append([int(parts[0]), int(parts[1])])
                elif len(parts) == 3:
                    matrix.append([parts[0], int(parts[1]), int(parts[2])])
            else:
                matrix.append([])


def print_matrix(local_matrix):
    for row in local_matrix:
        print(row)


def create_local_matrix():
    weight_limit = 0
    num_of_items = 0
    local_matrix: list[list[str | int]] = []
    for row in matrix:
        line = row.copy()
        if line:
            if len(line) == 2:
                weight_limit = int(line[1])
                num_of_items = int(line[0])
            elif len(line) == 3:
                local_matrix.append(line)
        else:
            break
    return local_matrix, weight_limit, num_of_items


def sort_by_value(local_matrix: list[list[str | int]]):
    return sorted(local_matrix, key=lambda x: x[2], reverse=True)


def sort_by_weight(local_matrix: list[list[str | int]]):
    return sorted(local_matrix, key=lambda x: x[1])


def sort_by_ratio(local_matrix: list[list[str | int]]):
    return sorted(local_matrix, key=lambda x: int(x[2]) / int(x[1]), reverse=True)


def greedy_value():
    print("Greedy by value:")
    current_weight: int = 0
    total_value: int = 0
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    items_gathered = []  # collect a list of which items we took for later use

    local_matrix = sort_by_value(local_matrix)
    # loop through the matrix until the weight limit is reached.
    for row in local_matrix:
        if check_timeout():
            return
        id: str = str(row[0])
        weight: int = int(row[1])
        value: int = int(row[2])

        # if we have enough space in our knapsack then take the value
        if current_weight + weight <= weight_limit:
            current_weight += weight
            total_value += value
            items_gathered.append(id)

    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {current_weight}")
    print(f"The total value collected: {total_value}")


def greedy_weight():
    print("Greedy by weight:")
    current_weight: int = 0
    total_value: int = 0
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    items_gathered = []  # collect a list of which items we took for later use

    local_matrix = sort_by_weight(local_matrix)
    # loop through the matrix until the weight limit is reached.
    for row in local_matrix:
        if check_timeout():
            return
        id: str = str(row[0])
        weight: int = int(row[1])
        value: int = int(row[2])

        # if we have enough space in our knapsack then take the value
        if current_weight + weight <= weight_limit:
            current_weight += weight
            total_value += value
            items_gathered.append(id)

    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {current_weight}")
    print(f"The total value collected: {total_value}")


def greedy_ratio():
    print("Greedy by ratio:")
    current_weight: int = 0
    total_value: int = 0
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    items_gathered = []  # collect a list of which items we took for later use

    local_matrix = sort_by_ratio(local_matrix)
    # loop through the matrix until the weight limit is reached.
    for row in local_matrix:
        if check_timeout():
            return
        id: str = str(row[0])
        weight: int = int(row[1])
        value: int = int(row[2])

        # if we have enough space in our knapsack then take the value
        if current_weight + weight <= weight_limit:
            current_weight += weight
            total_value += value
            items_gathered.append(id)

    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {current_weight}")
    print(f"The total value collected: {total_value}")


def optimized_dp():
    print("Optimized DP:")
    local_matrix, weight_limit, num_of_items = create_local_matrix()

    if weight_limit <= 0 or not local_matrix:
        print(f"Weight limit: {weight_limit}")
        print([])
        print("Ending weight: 0")
        print("The total value collected: 0")
        return

    dp = [0] * (weight_limit + 1)
    dp_node = [-1] * (weight_limit + 1)
    nodes: list[tuple[int, int]] = []

    for i, row in enumerate(local_matrix):
        if check_timeout():
            return
        weight = int(row[1])
        value = int(row[2])
        if weight <= 0:
            continue
        for w in range(weight_limit, weight - 1, -1):
            if check_timeout():
                return
            candidate = dp[w - weight] + value
            if candidate > dp[w]:
                dp[w] = candidate
                nodes.append((dp_node[w - weight], i))
                dp_node[w] = len(nodes) - 1

    best_weight = max(range(weight_limit + 1), key=lambda w: dp[w])
    total_value = dp[best_weight]

    items_gathered = []
    node_index = dp_node[best_weight]
    while node_index != -1:
        prev_node, item_index = nodes[node_index]
        items_gathered.append(str(local_matrix[item_index][0]))
        node_index = prev_node

    items_gathered.reverse()
    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {best_weight}")
    print(f"The total value collected: {total_value}")


def fptas_dp(eps: float = 0.1):
    print(f"FPTAS DP (eps={eps}):")
    local_matrix, weight_limit, num_of_items = create_local_matrix()

    if weight_limit <= 0 or not local_matrix:
        print(f"Weight limit: {weight_limit}")
        print([])
        print("Ending weight: 0")
        print("The total value collected: 0")
        return

    values = [int(row[2]) for row in local_matrix]
    max_value = max(values)
    if max_value <= 0:
        print(f"Weight limit: {weight_limit}")
        print([])
        print("Ending weight: 0")
        print("The total value collected: 0")
        return

    eps = max(eps, 1e-6)
    scale = (eps * max_value) / max(len(values), 1)
    if scale <= 0:
        scale = 1.0

    scaled_values = [max(1, int(v / scale)) for v in values]
    total_scaled_value = sum(scaled_values)

    inf = weight_limit + max(int(row[1]) for row in local_matrix) + 1
    dp = [inf] * (total_scaled_value + 1)
    dp_node = [-1] * (total_scaled_value + 1)
    nodes: list[tuple[int, int]] = []
    dp[0] = 0

    for i, row in enumerate(local_matrix):
        if check_timeout():
            return
        weight = int(row[1])
        value_scaled = scaled_values[i]
        if weight <= 0:
            continue
        for v in range(total_scaled_value, value_scaled - 1, -1):
            if check_timeout():
                return
            candidate = dp[v - value_scaled] + weight
            if candidate < dp[v] and candidate <= weight_limit:
                dp[v] = candidate
                nodes.append((dp_node[v - value_scaled], i))
                dp_node[v] = len(nodes) - 1

    best_value_scaled = 0
    for v in range(total_scaled_value, -1, -1):
        if dp[v] <= weight_limit:
            best_value_scaled = v
            break

    items_gathered = []
    node_index = dp_node[best_value_scaled]
    while node_index != -1:
        prev_node, item_index = nodes[node_index]
        items_gathered.append(str(local_matrix[item_index][0]))
        node_index = prev_node

    items_gathered.reverse()
    ending_weight = dp[best_value_scaled] if best_value_scaled > 0 else 0
    total_value = 0
    for item_id in items_gathered:
        for row in local_matrix:
            if str(row[0]) == item_id:
                total_value += int(row[2])
                break

    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {ending_weight}")
    print(f"The total value collected: {total_value}")


def brute_force():
    print("Brute Force:")
    all_items_gathered.clear()
    local_matrix, weight_limit, num_of_items = create_local_matrix()
    all_items_gathered.clear()

    create_permutations(0, local_matrix, [])
    if timed_out:
        return

    ending_weight = 0
    highest_value_seen = 0
    items_gathered = []

    for perm in all_items_gathered:
        if check_timeout():
            return
        # print(f"Permutation: {perm}")
        current_weight = 0
        total_value = 0
        for item_index in perm:
            item_weight = int(local_matrix[item_index][1])
            item_value = int(local_matrix[item_index][2])
            if current_weight + item_weight <= weight_limit:
                current_weight += item_weight
                total_value += item_value
                if total_value > highest_value_seen:
                    highest_value_seen = total_value
                    ending_weight = current_weight
                    items_gathered.clear()
                    for index in perm:
                        items_gathered.append(str(local_matrix[index][0]))

    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {ending_weight}")
    print(f"The total value collected: {highest_value_seen}")


def create_permutations(
    steps: int, matrix: list[list[str | int]], items_gathered: list[int]
):
    if check_timeout():
        return
    if steps >= len(matrix):
        global all_items_gathered
        all_items_gathered.append(items_gathered.copy())
        return

    new_gathered: list[int] = items_gathered.copy()
    new_gathered.append(steps)

    steps += 1

    create_permutations(steps, matrix, items_gathered.copy())
    create_permutations(steps, matrix, new_gathered)


def better_brute_force():
    all_items_gathered.clear()
    print("Better Brute Force:")
    local_matrix, weight_limit, num_of_items = create_local_matrix()

    better_trees(0, local_matrix, [], weight_limit)
    if timed_out:
        return

    ending_weight = 0
    highest_value_seen = 0
    items_gathered = []

    for perm in all_items_gathered:
        if check_timeout():
            return
        # print(f"Permutation: {perm}")
        current_weight = 0
        total_value = 0
        for item_index in perm:
            item_weight = int(local_matrix[item_index][1])
            item_value = int(local_matrix[item_index][2])
            current_weight += item_weight
            total_value += item_value
        if total_value > highest_value_seen:
            highest_value_seen = total_value
            ending_weight = current_weight
            items_gathered.clear()
            for index in perm:
                items_gathered.append(str(local_matrix[index][0]))

    print(f"Weight limit: {weight_limit}")
    print(items_gathered)
    print(f"Ending weight: {ending_weight}")
    print(f"The total value collected: {highest_value_seen}")


def better_trees(
    steps: int,
    matrix: list[list[str | int]],
    items_gathered: list[int],
    weight_limit: int,
):
    if check_timeout():
        return
    # check if this path is still within weight constraint
    current_weight = 0
    for item_index in items_gathered:
        item_weight = int(matrix[item_index][1])
        current_weight += item_weight

    # if we are over weight limit, stop exploring this path
    if current_weight > weight_limit:
        return

    # if we perfectly hit the limit, capture the current path and stop
    if current_weight == weight_limit:
        # global all_items_gathered
        all_items_gathered.append(items_gathered.copy())
        return

    if steps >= len(matrix):
        # global all_items_gathered
        all_items_gathered.append(items_gathered.copy())
        return

    new_gathered: list[int] = items_gathered.copy()
    new_gathered.append(steps)

    steps += 1

    better_trees(steps, matrix, items_gathered.copy(), weight_limit)
    better_trees(steps, matrix, new_gathered, weight_limit)


def start_timer():
    global time_start
    time_start = time.time()


def stop_timer():
    time_end = time.time()
    print(f"time elapsed: {time_end - time_start}")
    print()


def set_deadline(seconds: int):
    global deadline_time, timed_out
    deadline_time = time.time() + seconds
    timed_out = False


def check_timeout():
    global timed_out
    if timed_out:
        return True
    if time.time() >= deadline_time:
        timed_out = True
        return True
    return False


def run_with_limit(seconds: int, func):
    set_deadline(seconds)
    start_timer()
    func()
    stop_timer()
    if timed_out:
        print(f"Timed out after {seconds} seconds")
        print()


def main():
    global kp_files
    if len(sys.argv) <= 1:
        print("need more args")
        sys.exit(1)
    else:
        for arg in sys.argv[1:]:
            kp_files.append(arg)

    for kp_file in kp_files:
        matrix.clear()
        print(f"{kp_file}")
        read_file(kp_file)

        run_with_limit(300, greedy_value)
        run_with_limit(300, greedy_weight)
        run_with_limit(300, greedy_ratio)
        run_with_limit(300, optimized_dp)
        run_with_limit(300, fptas_dp)
        run_with_limit(120, better_brute_force)
        run_with_limit(120, brute_force)


if __name__ == "__main__":
    main()
