class stack:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        if self.item == [] :
            return True
        return False

if __name__ == "__main__" :
    st = stack()
    st.push(35)
    st.push(26)
    st.push(36)
    st.push(99)
    st.pop()
    st.push(69)
    st.push(66)
    st.push(70)
    st.pop()
    st.push(60)

while not st.is_empty():
    item = st.pop()
    print(item)