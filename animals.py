import animals.ferma_class as frm

if __name__ == '__main__':
    farm = frm.Farm()
    print(farm.generate("Dog"))
    print(farm.generate("fish"))
    print(farm.generate("Dog"))
    print(farm.generate("fish"))
    print(farm.generate("BIRD"))

    print(f"Всего животных\n{farm.get_info()}")
