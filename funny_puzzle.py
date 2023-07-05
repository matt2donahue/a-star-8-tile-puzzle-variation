import heapq
import copy


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    INPUT:
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0

    for i in range(len(from_state)):
        if from_state[i] != 0:
            from_x = 0
            from_y = 0
            to_x = 0
            to_y = 0
            if from_state[i] != to_state[i]:
                from_x = i % 3
                from_y = int(i / 3)

                for j in range(len(to_state)):
                    if from_state[i] == to_state[j]:
                        to_x = j % 3
                        to_y = int(j / 3)
            distance = distance + (abs(from_x - to_x) + abs(from_y - to_y))

    return distance


def print_succ(state):
    """
    INPUT:
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle.
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    INPUT:
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below).
    """
    succ_states = []

    for i in range(len(state)):
        if state[i] == 0:
            if i // 3 == 0:
                if i % 3 == 0:
                    if state[i + 1] != 0:
                        state[i] = state[i + 1]
                        state[i + 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 1] = state[i]
                        state[i] = 0
                    if state[i + 3] != 0:
                        state[i] = state[i + 3]
                        state[i + 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 3] = state[i]
                        state[i] = 0
                if i % 3 == 1:
                    if state[i + 1] != 0:
                        state[i] = state[i + 1]
                        state[i + 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 1] = state[i]
                        state[i] = 0
                    if state[i + 3] != 0:
                        state[i] = state[i + 3]
                        state[i + 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 3] = state[i]
                        state[i] = 0
                    if state[i - 1] != 0:
                        state[i] = state[i - 1]
                        state[i - 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 1] = state[i]
                        state[i] = 0
                if i % 3 == 2:
                    if state[i - 1] != 0:
                        state[i] = state[i - 1]
                        state[i - 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 1] = state[i]
                        state[i] = 0
                    if state[i + 3] != 0:
                        state[i] = state[i + 3]
                        state[i + 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 3] = state[i]
                        state[i] = 0

            elif i // 3 == 1:
                if i % 3 == 0:
                    if state[i + 1] != 0:
                        state[i] = state[i + 1]
                        state[i + 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 1] = state[i]
                        state[i] = 0
                    if state[i + 3] != 0:
                        state[i] = state[i + 3]
                        state[i + 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 3] = state[i]
                        state[i] = 0
                    if state[i - 3] != 0:
                        state[i] = state[i - 3]
                        state[i - 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 3] = state[i]
                        state[i] = 0
                if i % 3 == 1:
                    if state[i + 1] != 0:
                        state[i] = state[i + 1]
                        state[i + 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 1] = state[i]
                        state[i] = 0
                    if state[i + 3] != 0:
                        state[i] = state[i + 3]
                        state[i + 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 3] = state[i]
                        state[i] = 0
                    if state[i - 1] != 0:
                        state[i] = state[i - 1]
                        state[i - 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 1] = state[i]
                        state[i] = 0
                    if state[i - 3] != 0:
                        state[i] = state[i - 3]
                        state[i - 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 3] = state[i]
                        state[i] = 0
                if i % 3 == 2:
                    if state[i - 1] != 0:
                        state[i] = state[i - 1]
                        state[i - 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 1] = state[i]
                        state[i] = 0
                    if state[i + 3] != 0:
                        state[i] = state[i + 3]
                        state[i + 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 3] = state[i]
                        state[i] = 0
                    if state[i - 3] != 0:
                        state[i] = state[i - 3]
                        state[i - 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 3] = state[i]
                        state[i] = 0

            else:
                if i % 3 == 0:
                    if state[i + 1] != 0:
                        state[i] = state[i + 1]
                        state[i + 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 1] = state[i]
                        state[i] = 0
                    if state[i - 3] != 0:
                        state[i] = state[i - 3]
                        state[i - 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 3] = state[i]
                        state[i] = 0
                if i % 3 == 1:
                    if state[i + 1] != 0:
                        state[i] = state[i + 1]
                        state[i + 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i + 1] = state[i]
                        state[i] = 0
                    if state[i - 1] != 0:
                        state[i] = state[i - 1]
                        state[i - 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 1] = state[i]
                        state[i] = 0
                    if state[i - 3] != 0:
                        state[i] = state[i - 3]
                        state[i - 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 3] = state[i]
                        state[i] = 0
                if i % 3 == 2:
                    if state[i - 1] != 0:
                        state[i] = state[i - 1]
                        state[i - 1] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 1] = state[i]
                        state[i] = 0
                    if state[i - 3] != 0:
                        state[i] = state[i - 3]
                        state[i - 3] = 0
                        succ_states.append(copy.deepcopy(state))
                        state[i - 3] = state[i]
                        state[i] = 0

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    INPUT:
        An initial state (list of length 9)

    WHAT IT DOES:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    g = 0
    h = get_manhattan_distance(state)
    openpq = []
    closed = []
    parents = {}
    parent_index = 0
    reverse_path = {}
    # 1
    heapq.heappush(openpq, (g + h, state, (g, h, -1)))

    # 2
    while len(openpq) != 0:
        # 3
        n = heapq.heappop(openpq)
        parents[parent_index] = n
        parent_index = parent_index + 1
        closed.append(n)
        # print(parent_index)

        # 4
        if n[1] != goal_state:
            # 5
            n_prime = get_succ(n[1])
            # parents[parent_index] = n
            g_prime = n[2][0] + 1

            for next_state in n_prime:
                # check if on closed
                closed_val = 0
                for i in range(len(closed)):
                    if closed[i][1] == next_state:
                        closed_val = 1
                        break
                open_val = 0
                # check if on open
                for i in range(len(openpq)):
                    if openpq[i][1] == next_state:
                        if g_prime < openpq[i][2][0]:
                            temp_node = openpq[i][1]
                            # print(openpq[i])
                            openpq.pop(i)
                            h_prime = get_manhattan_distance(temp_node)
                            heapq.heappush(
                                openpq,
                                (
                                    g_prime + h_prime,
                                    temp_node,
                                    (g_prime, h_prime, n[2][2]),
                                ),
                            )
                            # openpq[i][0] = g_prime + openpq[i][2][1]
                            # openpq[i][2][0] = g_prime
                            open_val = 1
                            heapq.heapify(openpq)
                            break
                if closed_val == 0 and open_val == 0:
                    h_prime = get_manhattan_distance(next_state)
                    heapq.heappush(
                        openpq,
                        (
                            g_prime + h_prime,
                            next_state,
                            (g_prime, h_prime, parent_index - 1),
                        ),
                    )
        else:
            # print(closed)
            # print(parents)
            reverse_path[n[2][2]] = n
            while n[2][2] != -1:
                n = parents[n[2][2]]
                reverse_path[n[2][2]] = n
            break
    # print(reverse_path)
    for i in reversed(reverse_path):
        print(
            str(reverse_path[i][1])
            + " h="
            + str(reverse_path[i][2][1])
            + " moves: "
            + str(reverse_path[i][2][0])
        )
    print("Max queue length: " + str(len(openpq)))


if __name__ == "__main__":
    """
    Can insert your own puzzles to test, just follow the solve() and print() format below
    """
    print_succ([2, 5, 1, 4, 0, 6, 7, 0, 3])
    print()

    print(
        get_manhattan_distance([2, 5, 1, 4, 0, 6, 7, 0, 3], [1, 2, 3, 4, 5, 6, 7, 0, 0])
    )
    print()

    solve([2, 5, 1, 4, 0, 6, 7, 0, 3])
    print()

    solve([4, 3, 0, 5, 1, 6, 7, 2, 0])
    print()

    solve([3, 4, 6, 0, 0, 1, 7, 2, 5])
    print()

    solve([6, 0, 0, 3, 5, 1, 7, 2, 4])
    print()

    solve([0, 4, 7, 1, 3, 0, 6, 2, 5])
    print()

    solve([5, 2, 3, 0, 6, 4, 7, 1, 0])
    print()

    solve([1, 7, 0, 6, 3, 2, 0, 4, 5])
    print()
