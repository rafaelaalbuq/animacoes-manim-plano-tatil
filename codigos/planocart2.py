from manim import *
import numpy as np

class plano(MovingCameraScene):
    def construct(self):
        # 1. Configuração de Fundo e Logo
        cordefundo = ManimColor("#D5D5DD")
        self.camera.background_color = cordefundo

        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff=0.1)
            self.add(img)
        except:
            print('LOGO NAO ENCONTRADA')

        # 2. Título Inicial 
        titulo = Tex(r"A Reta Como Sequência De Pontos", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))

        #grade - eixos
        reta_X = NumberLine(x_range=[-10, 10], color=BLACK, stroke_width=2)
        reta_Y = NumberLine(x_range=[-10, 10], color=BLACK, stroke_width=2)
        
        grade = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={"stroke_color": BLACK, "stroke_width": 2}
        )


        self.camera.frame.save_state()
        self.camera.frame.set(width=17) 

        funcao_1 = MathTex(r"y = 2x", color=BLACK).scale(1.5).to_corner(UP+LEFT, buff=0.2)
        dom_1 = Tex(r"D = [-2,2]", color=PURE_BLUE).scale(1.5).next_to(funcao_1, DOWN, buff=0.5)
        dom_2 = MathTex(r"D = \mathbb{Z}", color=PURE_BLUE).scale(1.5).next_to(funcao_1, DOWN, buff=0.5)
        dom_3 = MathTex(r"D = \mathbb{R}", color=PURE_BLUE).scale(1.5).next_to(funcao_1, DOWN, buff=0.5)
        
        self.play(Write(dom_1), Write(funcao_1))
        self.play(Create(reta_X), Create(reta_Y))
        self.play(reta_Y.animate.rotate(90 * DEGREES, about_point=ORIGIN))
        self.play(FadeIn(grade))

        # 1: D = [-2, 2] (Apenas os extremos)
        p3_coords = [-2, -4, 0]
        p4_coords = [2, 4, 0]
        dot_c = Dot(p3_coords, color=PURE_RED)
        dot_d = Dot(p4_coords, color=PURE_RED)
        c_label = MathTex("C(-2, -4)", color=PURE_RED).scale(1).next_to(dot_c, LEFT, buff=0.1)
        d_label = MathTex("D(2, 4)", color=PURE_RED).scale(1).next_to(dot_d, RIGHT, buff=0.1)

        #tracejado do dot_c
        trace_c = DashedLine(start=dot_c.get_center(), end=[dot_c.get_center()[0], 0, 0], color=PURE_RED)
        trace_c2 = DashedLine(start=dot_c.get_center(), end=[0, dot_c.get_center()[1], 0], color=PURE_RED)

        #tracejado do dot_d
        trace_d = DashedLine(start=dot_d.get_center(), end=[dot_d.get_center()[0], 0, 0], color=PURE_RED)
        trace_d2 = DashedLine(start=dot_d.get_center(), end=[0, dot_d.get_center()[1], 0], color=PURE_RED)

        
        self.play(FadeIn(dot_c, scale=0.5), Create(trace_c), Create(trace_c2), Write(c_label))
        self.play(FadeIn(dot_d, scale=0.5), Create(trace_d), Create(trace_d2), Write(d_label))
        self.wait(2)
        
        
        self.play(FadeOut(trace_c), FadeOut(trace_c2), FadeOut(c_label), FadeOut(trace_d), FadeOut(trace_d2), FadeOut(d_label))


        # 2: D=Z (Preenchendo Inteiros)
        self.play(ReplacementTransform(dom_1, dom_2))
        self.wait()

        pontos_Z = VGroup()
        labels_Z = VGroup()
        traces_Z = VGroup()

       
        for x in range(-1, 2):
            y = 2 * x
            dot = Dot([x, y, 0], color=PURE_RED)
            label = MathTex(f"({x}, {y})", color=BLACK).scale(0.6).next_to(dot, DL, buff=0.1)
            
            trace = DashedLine(start=dot.get_center(), end=[x, 0, 0], color=PURE_RED, stroke_opacity=1)
            trace2 = DashedLine(start=dot.get_center(), end=[0, y, 0], color=PURE_RED, stroke_opacity=1)
            
            pontos_Z.add(dot)
            labels_Z.add(label)
            traces_Z.add(trace, trace2)

        # Pontos surgem um por um
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in pontos_Z], lag_ratio=0.2), Write(labels_Z))
        self.play(Create(traces_Z))
        self.wait(2)

        
        self.play(FadeOut(labels_Z), FadeOut(traces_Z))


        #3: D=R (preenchendo a reta com pontos)
        self.play(ReplacementTransform(dom_2, dom_3))
        self.wait()

        #Preenchendo as metades (0.5)
        pontos_metades = VGroup()
        for x in np.arange(-1.5, 2.0, 1.0): # Apenas os valores com .5
            y = 2 * x
            dot = Dot([x, y, 0], color=PURE_RED)
            pontos_metades.add(dot)

        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in pontos_metades], lag_ratio=0.1))
        self.wait(1)

        #pontos menores preenchendo os décimos (0.1)
        pontos_chuva = VGroup()
        for x in np.arange(-2.0, 2.1, 0.1):
            y = 2 * x
           
            dot = Dot([x, y, 0], color=PURE_RED).scale(0.8) 
            pontos_chuva.add(dot)

        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in pontos_chuva], lag_ratio=0.02), run_time=2)
        self.wait(1)

        # 3(Os pontos discretos se fundem na reta contínua)
        reta_real = Line(start=[-2, -4, 0], end=[2, 4, 0], color=PURE_BLUE, stroke_width=6)
        
        # Agrupando todos os pontos da tela
        todos_os_pontos = VGroup(dot_c, dot_d, pontos_Z, pontos_metades, pontos_chuva)
        
        #transformando os pontos na reta
        self.play(ReplacementTransform(todos_os_pontos, reta_real), run_time=1.5)
        
        self.wait(3)