import sys

def print_arr(arr, sizei, sizej):
    for i in range(0, sizei):
        for j in range(0, sizej + 1):
            print("%11s" % arr[i][j], end="\t")
        print()

def parse_inputs(sim_raw):
    sim_arr = []
    el_arr = sim_raw.split("|")
    for el in el_arr:
        sim_arr.append(el.split(","))
    return sim_arr

def parse_transitions(states_arr, symbols_arr, states_dictionary, symbols_dictionary):
    nka_arr = [[['#'] for i in range(len(symbols_arr)+1)] for j in range(len(states_arr))]
    for line in sys.stdin:
        temp = line[:-1].split("->")
        curr = temp[0].split(",")
        nxt = temp[1].split(",")
        nka_arr[ states_dictionary[curr[0]] ][ symbols_dictionary[curr[1]] ] = nxt
    return nka_arr

def build_state_dictionary(states_arr):
    thisdict = {}
    i = 0
    for el in states_arr:
        thisdict[el] = i
        i += 1
    return thisdict

def build_symbol_dictionary(symbols_arr): # -1: #, 0: a, 1: lab2, 2: pnp, 3: utr, 4: $
    thisdict = {}
    thisdict["#"] = -1
    i = 0
    for el in symbols_arr:
        thisdict[el] = i
        i += 1
    thisdict["$"] = len(symbols_arr)
    return thisdict

def recursive_epsilon_search(nka_arr, search_state, states_dict, col_len, visited, save_arr):
    if search_state not in visited and search_state != "#":
        save_arr.append(search_state)
        visited.add(search_state)
        ns_arr = nka_arr[states_dict[search_state]][col_len] # ns = next state
        for ns in ns_arr:
            recursive_epsilon_search(nka_arr, ns, states_dict, col_len, visited, save_arr)

def nka_sim_cols(nka_arr, state, states_dict, symbols_dict):
    arr = []
    for idx, el in enumerate(nka_arr[states_dict[state]]):
        if "#" in el:
            continue
        arr.append(idx)
    return arr

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
    
    curr_state = []
    next_state = []
    save_arr = []
    visited = set()
    state_exist = False
    for sim in sim_arr: # Jedinstvena simulacija
        recursive_epsilon_search(nka_arr, init_state, states_dictionary, len(symbols_arr), visited, curr_state)
        visited.clear()
        curr_state.sort()
        for idx, el in enumerate(curr_state):
            if idx == 0:
                print(el, end="")
            else:
                print("," + el, end="")
        for se in sim: # se = simulation element
            if("#" not in curr_state):
                for ce in curr_state: # ce = current state element
                    if symbols_dictionary[se] in nka_sim_cols(nka_arr, ce, states_dictionary, symbols_dictionary):
                        res = nka_arr[states_dictionary[ce]][symbols_dictionary[se]]
                        for el in res:
                            recursive_epsilon_search(nka_arr, el, states_dictionary, len(symbols_arr), visited, save_arr)
                            visited.clear()
                        next_state.extend(save_arr)
                        save_arr.clear()
                        state_exist = True
                # endfor
                if(state_exist == False):
                    next_state.append("#")
            else:
                next_state.append("#")
            next_state.sort() # Sortiraj listu
            next_state = list(dict.fromkeys(next_state)) # Makni duplikate
            for idx, el in enumerate(next_state):
                if idx == 0:
                    print("|" + el, end="")
                else:
                    print("," + el, end="")
            curr_state.clear()
            curr_state.extend(next_state)
            next_state.clear()
            state_exist = False
        #endfor
        print()
        curr_state.clear()
        next_state.clear()

if __name__ == "__main__":
    main()