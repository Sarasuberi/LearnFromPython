class Block:
    def __init__(self,tb_game) -> None:
        self.settings = tb_game.settings
        
    # 设置每个数值对应的块的颜色
    def getBlockColor(self,num:int):  
        match num:
            case 2:
                return (238, 228, 218)
            case 4:
                return (237, 224, 200)
            case 8:
                return (242, 177, 121)
            case 16:
                return (245, 149, 99)
            case 32:
                return (246, 124, 95)
            case 64:
                return (247, 96, 63)
            case 128:
                return (237, 209, 124)
            case 256:
                return (237, 206, 109)
            case 512:
                return (237, 203, 93)
            case 1024:
                return (237, 201, 79)
            case 2048:
                return (237, 197, 62)
            case 4096:
                return (249, 139, 73)
            case 8192:
                return (251, 132, 57)
            case 16384:
                return (252, 118, 38)
            case _:
                return (36, 36, 36)
    