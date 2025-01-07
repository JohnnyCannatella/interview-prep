
# LINKED LIST
Una linked list normale è una sequenza di nodi dove ogni nodo punta al successivo, e l'ultimo nodo punta a null:
1 -> 2 -> 3 -> 4 -> null

Una linked list con un ciclo è quando un nodo, invece di puntare a null, punta a un nodo precedente nella lista, creando un "loop" infinito:
 1 -> 2 -> 3 -> 4
 ^         |
 |_________|

in una linked list conosco solo il .next e non so mai chi è il precedente
Non ho la lunghezza della lista -> len(head) non posso farlo
Non è sortable