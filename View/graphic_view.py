# -*- coding: utf-8 -*-

class Graphic:
    def __init__(self, canvas, x, y, x_label, y_label):
        self.my_canvas = canvas
        self.x = x
        self.y = y
        self.x_label = x_label
        self.y_label = y_label
        self._line2D = None

    def plot(self):
        self.my_canvas.axes.clear()

        self.my_canvas.axes.grid(color='green', linestyle='--', linewidth=0.5)

        self._line2D, = self.my_canvas.axes.plot(self.x, self.y,
                                                 color='r', lw=1., markersize=5, marker='+',
                                                 picker=30)

        self.my_canvas.axes.set_xlabel(self.x_label, color='black', fontsize=10)
        self.my_canvas.axes.set_ylabel(self.y_label, color='black', fontsize=10)

        al = 8.  # arrow length in points
        arrowprops = dict(clip_on=True,  # plotting outside axes on purpose
                          #    frac=1.,  # make end arrowhead the whole size of arrow
                          headwidth=5.,  # in points
                          facecolor='k')
        kwargs = dict(
            xycoords='axes fraction',
            textcoords='offset points',
            arrowprops=arrowprops,
        )
        self.my_canvas.axes.annotate("", (1, 0), xytext=(-al, 0), **kwargs)
        self.my_canvas.axes.annotate("", (0, 1), xytext=(0, -al), **kwargs)  # left spin arrow
        # self.my_canvas.axes.spines[['top', 'right']].set_visible(
        #     False)  # pour enlever le 'cadre' en haut et à droite de la figure
        self.my_canvas.axes.spines[['top', 'right']].set_color('none')
        self.my_canvas.axes.yaxis.tick_left()  # enlève les traits de graduation sur le côté gauche du graphique
        self.my_canvas.axes.xaxis.tick_bottom()  # enlève les traits de graduation sur la partie supérieure du graphique
        self.my_canvas.axes.set_facecolor('#F9F9F9')  # '#E0FFFF')
        self.my_canvas.figure.patch.set_facecolor('white')
        self.my_canvas.figure.tight_layout()

        self.my_canvas.figure.canvas.draw_idle()
