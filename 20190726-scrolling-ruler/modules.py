class RulerModule:
    def __init__(self, numbers, outline, line_width, font_size, r):
        self.numbers = numbers
        self.displaying = []
        self.normalised = []
        self.circle_refs = []
        self.text_refs = []
        self.line_refs = []

        self.outline = outline
        self.width = line_width
        self.font_size = font_size
        self.r = r

    def render_region(self, lower, upper, canvas, w, h):
        self.displaying = [n for n in self.numbers if n < upper and n > lower]
        normalised = [(n - lower) / (upper - lower) for n in self.displaying]

        if len(self.normalised) < len(normalised):
            for _ in range(0, len(normalised) - len(self.normalised)):
                self.circle_refs.append(canvas.create_oval(
                    (0, 0, 1, 1), outline=self.outline, width=self.width))
                self.text_refs.append(canvas.create_text(
                    (0, 0), text="", fill=self.outline, font="Arial {}".format(self.font_size)))
                self.line_refs.append(canvas.create_line(
                    (0, 0, 1, 1), fill=self.outline, width=self.width))
        elif len(self.normalised) > len(normalised):
            for _ in range(0, len(self.normalised) - len(normalised)):
                c = self.circle_refs.pop()
                canvas.delete(c)
                t = self.text_refs.pop()
                canvas.delete(t)
                l = self.line_refs.pop()
                canvas.delete(l)

        self.normalised = normalised

        xs = [n * w for n in self.normalised]
        ys = 0.5 * h
        r = self.r
        start = 0
        for i, _ in enumerate(self.normalised):
            circle_coords = (xs[i] - r, ys - r, xs[i] + r, ys + r)
            canvas.coords(self.circle_refs[i], circle_coords)
            text_coords = (xs[i], ys)
            canvas.coords(self.text_refs[i], text_coords)
            canvas.itemconfig(self.text_refs[i], text=self.displaying[i])
            line_coords = (start, ys, xs[i] - r, ys)
            canvas.coords(self.line_refs[i], line_coords)
            start = xs[i] + r
        else:
            line_coords = (xs[i] + r, ys, w, ys)
            try:
                canvas.coords(self.line_refs[i + 1], line_coords)
            except IndexError:
                self.line_refs.append(canvas.create_line(
                    line_coords, fill=self.outline, width=self.width))
