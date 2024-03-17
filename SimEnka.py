import sys
import numpy as np

def parse_transitions(states_arr, symbols_arr):
    """
    Parsira ``linije prijelaza`` u polje velicine ``[skup_stanja X skup_stanja]``
    Format linije: [trenutno_stanje, delta -> trenutno_stanje1, trenutno_stanje2, ...]

    Parameters
    ----------
    nka_transition_array : string_array
        Polje u koje se spremaju parsirani rezultat
    states_arr : string_array
        Polje stanja
    symbols_arr : string_array
        Polje simbola
    
    Returns
    -------
    nka_transition_array : string_array
        Polje u koje se spremaju parsirani rezultat
    """
    nka_transition_array = np.full([states_arr.size, states_arr.size], fill_value=-1)
    for line in sys.stdin:
        temp = line[:-1].split("->")
        currstate_delta = temp[0].split(",")
        next_states = temp[1].split(",")
        if np.isin("#", next_states):
            continue
        current_state_id = np.searchsorted(states_arr, currstate_delta[0])
        for el in np.searchsorted(states_arr, next_states):
            nka_transition_array[current_state_id][el] = np.searchsorted(symbols_arr, currstate_delta[1])
    return nka_transition_array

def parse_inputs(sim_raw):
    sim_arr = []
    el_arr = sim_raw.split("|")
    for el in el_arr:
        sim_arr.append(el.split(","))
    return sim_arr

def main():
    sim_raw = input("")
    states_raw = input("")
    symbols_raw = input("")
    acc_states_raw = input("")
    init_state = input("")

    sim_arr = parse_inputs(sim_raw)

    states_arr = np.array(states_raw.split(","))
    symbols_arr = np.array(symbols_raw.split(","))
    symbols_arr = np.insert(symbols_arr, 0, '$', axis=0)
    acc_states_arr = np.array(acc_states_raw.split(","))

    nka_arr = parse_transitions(states_arr, symbols_arr)

    print(nka_arr)
    print(np.searchsorted(nka_arr[2], 4))

    state_stack = []
    init_state_id = np.searchsorted(states_arr, init_state)
    for sim_instance in sim_arr:
        state_stack.append(init_state_id)
        print(states_arr[init_state_id], end="")
        sim_indexes = np.searchsorted(symbols_arr, sim_instance)
        for si in sim_indexes:
            print("|", end="")
            
        print()

if __name__ == "__main__":
    main()