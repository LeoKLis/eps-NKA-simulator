import sys

def print_arr(arr, sizei, sizej):
    for i in range(0, sizei):
        for j in range(0, sizej + 1):
            print("%11s" % arr[i][j], end="\t")
        print()

def parse_transitions(states_arr, symbols_arr, states_dictionary, symbols_dictionary):
    nka_arr = [[['#'] for i in range(len(symbols_arr)+1)] for j in range(len(states_arr))]
    for line in sys.stdin:
        temp = line[:-1].split("->")
        curr = temp[0].split(",")
        nxt = temp[1].split(",")
        nka_arr[ states_dictionary[curr[0]] ][ symbols_dictionary[curr[1]] ] = nxt
    return nka_arr

def parse_inputs(sim_raw):
    sim_arr = []
    el_arr = sim_raw.split("|")
    for el in el_arr:
        sim_arr.append(el.split(","))
    return sim_arr

def build_state_dictionary(states_arr):
    thisdict = {}
    i = 0
    for el in states_arr:
        thisdict[el] = i
        i += 1
    return thisdict

def build_symbol_dictionary(symbols_arr):
    thisdict = {}
    thisdict["#"] = -1
    i = 0
    for el in symbols_arr:
        thisdict[el] = i
        i += 1
    thisdict["$"] = len(symbols_arr)
    return thisdict

def main():
    sim_raw = input("")
    states_raw = input("")
    symbols_raw = input("")
    acc_states_raw = input("")
    init_state = input("")

    sim_arr = parse_inputs(sim_raw)

    states_arr = states_raw.split(",")
    states_dictionary = build_state_dictionary(states_arr)

    symbols_arr = symbols_raw.split(",")
    symbols_dictionary = build_symbol_dictionary(symbols_arr)

    nka_arr = parse_transitions(states_arr, symbols_arr, states_dictionary, symbols_dictionary)
    
    print_arr(nka_arr, len(states_arr), len(symbols_arr))    
    print(sim_arr)

    curr_state = []
    for sim in sim_arr:
        curr_state.append(init_state)
        print(curr_state[0], end="")
        for el in sim:
            if(curr_state != ["#"]):
                #stao ovdje!!    
                #curr_state = nka_arr[states_dictionary[curr_state]][symbols_dictionary[el]]

                for i in range(0, len(curr_state)):
                    if i == 0:
                        print("|" + curr_state[i], end="")
                    else:
                        print("," + curr_state[i], end="")
        print()
        curr_state.clear()


if __name__ == "__main__":
    main()