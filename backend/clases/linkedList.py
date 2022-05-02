class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None

    def __str__(self):
        return str(self.Value)

    def __repr__(self):
        return self.Value
    
    def __iter__(self):
         return self.Value

class LinkedList: 
    
    def __init__(self):
        self.First = None
        self.Size = 0

    def __iter__(self):
        node = self.First
        while node is not None:
            yield node.Value
            node = node.Next

    def __len__(self):
        return self.Size

    def __str__(self):
        String = "["
        Current = self.First
        for i in range(len(self)):
            String += str(Current)
            if i != len(self) - 1:
                 String += str(", ")
            Current = Current.Next
        String += "]"
        
        return String
    
    def __setitem__(self, indice, Value):
        if indice >= 0 and indice < self.Size:
            actual = self.First

            for _ in range(indice):
                actual = actual.Next
            
            actual.Value = Value
        else:
            return False
            #raise Exception('Índice no válido. Está por fuera del rango.')

   
    def __getitem__(self, index):
        if index >= 0 and index < self.Size:
            actual = self.First
            for i in range(index):
                actual = actual.Next
            return actual.Value
        else:
            return False
            #raise Exception('Índice no válido. Está por fuera del rango.')

    def Append(self, Value): 
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        
        else:
            Current = self.First
            while Current.Next != None:
                 Current = Current.Next
            Current.Next = MyNode
        self.Size += 1
        
        return MyNode
    
    def Pop(self):
        if self.Size == 0:
            return ''
        else:
            DeletedNode = self.First
            self.First = self.First.Next
        self.Size -= 1
        return DeletedNode.Value

    def Remove(self, Value):
        actual = self.First
        anterior = self.First
        eliminado = False

        if actual is None:
            eliminado = False
        elif actual.Value == Value:
            self.First = actual.Next
            eliminado = True
        else:
            while actual:
                if actual.Value == Value:
                    # Antes: 2 = 3 = 5 = 7 = 11
                    # Actual: 3
                    # Después: 2 = 5 = 7 = 11
                    anterior.Next = actual.Next
                    eliminado = True
                anterior = actual
                actual = actual.Next
        
        if eliminado:
            self.Size -= 1


    def Buscar(self, Value):
        if self.Size == 0:
            return False
        else:
            Current = self.First
            try:
                 while Current.Next.Value != Value:
                     Current = Current.Next
                 return True
            except AttributeError:
                 return False

        
        
