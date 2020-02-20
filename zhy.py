def visualize(self, size=20, grid=1, outerPath=None):
    # INPUT ARGS:
    # int size in [0 : inf]: block size(width and height)
    # int grid in [0 : size//2]: grid width
    # list outerPath with element (row, col): a path from S to G. None or [] if not exist
    # RETURN VALUE:
    # PIL.Image.Image img with mode = RGB: hi-res output maze map

    def gridOn(image, size=20, grid=1, color=64, beacon=64, distance=16):
        # np.array image with ndim = 2: output maze map image
        # int color in [0 : 255]: grid color #TODO: adapt to chromatic image
        # int beacon in [0 : 255]: beacon gird for every 64 blocks

        for row in range(self.rows):
            if not bool(row % distance):  # beacon
                image[row * size: row * size + grid + 1, :, :] = beacon
                image[row * size + size - grid - 1: row * size + size, :, :] = beacon
            else:
                image[row * size: row * size + grid, :, :] = color
                image[row * size + size - grid: row * size + size, :, :] = color

        for col in range(self.cols):
            if not bool(col % distance):  # beacon
                image[:, col * size: col * size + grid + 1, :] = beacon
                image[:, col * size + size - grid - 1: col * size + size, :] = beacon
            else:
                image[:, col * size: col * size + grid, :] = color
                image[:, col * size + size - grid: col * size + size, :] = color
        return

    if outerPath:
        path = outerPath
    else:
        path = self.path

    image = np.zeros((self.rows * size, self.cols * size, 3), dtype=np.uint8)
    # wall
    for row in range(self.rows):
        for col in range(self.cols):
            if self.wall[row, col]:
                image[row * size + grid: row * size + size - grid, col * size + grid: col * size + size - grid] = 255
    # closed
    if hasattr(self, 'closed') and self.closed is not None:
        cColor = [81, 88, 12]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.closed[row, col]:
                    image[row * size: row * size + size, col * size: col * size + size] = cColor
    # grid
    if grid != 0:
        gridOn(image, size, grid, color=64)
    # path
    if path:
        sColor = [82, 172, 118]
        gColor = [195, 239, 172]
        beacon = [82, 158, 118]
        distance = 32
        rStart = sColor[0]
        gStart = sColor[1]
        bStart = sColor[2]
        rDist = gColor[0] - sColor[0]
        gDist = gColor[1] - sColor[1]
        bDist = gColor[2] - sColor[2]
        length = len(path)
        prevRow = self.start[0]
        prevCol = self.start[1]
        for i in range(length):
            row = path[i][0]
            col = path[i][1]
            if not bool(i % distance):
                image[row * size + grid: row * size + size - grid, col * size + grid: col * size + size - grid] = beacon
            else:
                image[row * size + grid: row * size + size - grid, col * size + grid: col * size + size - grid] = (
                rStart + i * rDist // length, gStart + i * gDist // length, bStart + i * bDist // length)
            if prevRow + 1 == row:  # D
                image[row * size - grid: row * size + grid, col * size + grid: col * size + size - grid] = (
                rStart + i * rDist // length, gStart + i * gDist // length, bStart + i * bDist // length)
            if prevRow - 1 == row:  # U
                image[row * size + size - grid: row * size + size + grid,
                col * size + grid: col * size + size - grid] = (
                rStart + i * rDist // length, gStart + i * gDist // length, bStart + i * bDist // length)
            if prevCol + 1 == col:  # R
                image[row * size + grid: row * size + size - grid, col * size - grid: col * size + grid] = (
                rStart + i * rDist // length, gStart + i * gDist // length, bStart + i * bDist // length)
            if prevCol - 1 == col:  # L
                image[row * size + grid: row * size + size - grid,
                col * size + size - grid: col * size + size + grid] = (
                rStart + i * rDist // length, gStart + i * gDist // length, bStart + i * bDist // length)
            prevRow = row
            prevCol = col
    else:
        # start & goal
        sgColor = [82, 158, 118]
        backColor = 0
        for block in [self.start, self.goal]:
            row = block[0]
            col = block[1]
            image[row * size + grid: row * size + size - grid, col * size + grid: col * size + size - grid] = sgColor
            # break outer wall
            if row == 0:  # first row, break wall U
                image[0: grid, col * size + grid: col * size + size - grid] = backColor
            if row == self.rows - 1:  # last row, break wall D
                image[row * size + size - grid: row * size + size,
                col * size + grid: col * size + size - grid] = backColor
            if col == 0:  # first col, break wall L
                image[row * size + grid: row * size + size - grid, 0: grid] = backColor
            if col == self.cols - 1:  # last col, break wall R
                image[row * size + grid: row * size + size - grid,
                col * size + size - grid: col * size + size] = backColor
    # plot image
    img = Image.fromarray(image)
    img = ImageChops.invert(img)
    plt.imshow(img)
    plt.show()  # TODO: non-block call
    return img