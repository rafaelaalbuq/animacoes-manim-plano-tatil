from manim import *

class EsbocoGrafico(MovingCameraScene):
    def construct(self):
       
        self.camera.background_color = WHITE
        
       
       
       
        titulo = Tex("Guia de Esboço de Gráfico", color=BLACK, font_size=72).to_edge(UP)
        passos = VGroup(
            Tex("1. Concavidade ($a$)", color=BLACK),
            Tex("2. Intercepto $y$ ($c$)", color=PURE_GREEN),
            Tex("3. Raízes ($x_1$ e $x_2$)", color=PURE_RED),
            Tex("4. Vértice ($V$)", color=PURE_BLUE),
            Tex("5. Esboçar a curva", color=BLACK)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(1.2)

        self.play(Write(titulo))
        self.play(FadeIn(passos, shift=UP))
        self.wait(2)
        self.play(FadeOut(titulo), FadeOut(passos))

       
        # 1 f(x) = x^2 - 4x + 3 (Concavidade para CIMA)
        
        self.animar_esboco(
            func_tex="f(x) = x^2 - 4x + 3",
            a=1, b=-4, c=3,
            raizes=[1, 3],
            xv=2, yv=-1,
            cor=PURE_BLUE
        )

        self.clear()

        # 2 f(x) = -x^2 - 2x + 3 (Concavidade para BAIXO)
       
        self.animar_esboco(
            func_tex="f(x) = -x^2 - 2x + 3",
            a=-1, b=-2, c=3,
            raizes=[-3, 1],
            xv=-1, yv=4,
            cor=PURE_RED
        )

    def animar_esboco(self, func_tex, a, b, c, raizes, xv, yv, cor):
       
        grade = NumberPlane(
            x_range=[-6, 6, 1], y_range=[-6, 6, 1], x_length=7, y_length=7,
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.5},
            axis_config={"stroke_color": BLACK, "stroke_width": 2, "include_numbers": True}
        ).to_edge(RIGHT)
        grade.get_x_axis().numbers.set_color(BLACK)
        grade.get_y_axis().numbers.set_color(BLACK)

        titulo_func = MathTex(func_tex, color=BLACK, font_size=54).to_corner(UL)
        self.play(Write(titulo_func), FadeIn(grade))

        # 1: Concavidade 
        txt_a = Tex(f"1. $a = {a} > 0 \\rightarrow$ CIMA" if a>0 else f"1. $a = {a} < 0 \\rightarrow$ BAIXO", 
                    color=BLACK, font_size=40).next_to(titulo_func, DOWN, aligned_edge=LEFT, buff=0.5)
        icone_a = MathTex("\\cup" if a>0 else "\\cap", color=BLACK, font_size=80).next_to(txt_a, RIGHT)
        self.play(Write(txt_a), FadeIn(icone_a))
        self.wait(0.5)

        # 2: Intercepto y 
        txt_c = Tex(f"2. Intercepto $y$: $(0, {c})$", color=PURE_GREEN, font_size=40).next_to(txt_a, DOWN, aligned_edge=LEFT)
        ponto_c = Dot(grade.c2p(0, c), color=PURE_GREEN, radius=0.15)
        
        self.play(Write(txt_c))
        self.play(self.camera.frame.animate.scale(0.5).move_to(ponto_c), run_time=1.2) # Zoom no Intercepto
        self.play(FadeIn(ponto_c), Flash(ponto_c, color=PURE_GREEN, line_length=0.3))
        self.wait(0.5)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN)) # Volta ao normal

        # 3: Raízes (Bolinhas Vermelhas)
        txt_raizes = Tex(f"3. Raízes: ${raizes[0]}$ e ${raizes[1]}$", color=PURE_RED, font_size=40).next_to(txt_c, DOWN, aligned_edge=LEFT)
        p1 = Dot(grade.c2p(raizes[0], 0), color=PURE_RED, radius=0.15)
        p2 = Dot(grade.c2p(raizes[1], 0), color=PURE_RED, radius=0.15)
        
        self.play(Write(txt_raizes))
        # Zoom focado na base das raízes
        meio_raizes = grade.c2p((raizes[0]+raizes[1])/2, 0)
        self.play(self.camera.frame.animate.scale(0.6).move_to(meio_raizes), run_time=1.2)
        self.play(FadeIn(p1, p2))
        self.play(Flash(p1, color=PURE_RED), Flash(p2, color=PURE_RED))
        self.wait(0.5)
        self.play(self.camera.frame.animate.scale(1/0.6).move_to(ORIGIN))

        #4: Vértice 
        txt_v = Tex(f"4. Vértice: $V({xv}, {yv})$", color=PURE_BLUE, font_size=40).next_to(txt_raizes, DOWN, aligned_edge=LEFT)
        p_v = Dot(grade.c2p(xv, yv), color=PURE_BLUE, radius=0.15)
        rastro_v = DashedLine(grade.c2p(xv, 0), grade.c2p(xv, yv), color=GRAY)
        
        self.play(Write(txt_v))
        self.play(self.camera.frame.animate.scale(0.5).move_to(p_v), run_time=1.2) # Zoom no Vértice
        self.play(Create(rastro_v), FadeIn(p_v))
        self.play(Flash(p_v, color=PURE_BLUE))
        self.wait(0.5)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))

        #5: Esboço e Enquadramento Final
        txt_fim = Tex("5. Esboçar a Curva", color=BLACK, font_size=45).next_to(txt_v, DOWN, aligned_edge=LEFT, buff=0.6)
        parabola = grade.plot(lambda x: a*x**2 + b*x + c, x_range=[xv-3, xv+3], color=cor, stroke_width=8)
        
        self.play(Write(txt_fim))
        self.play(Create(parabola), run_time=2.5)

        
        pontos_importantes = VGroup(p1, p2, p_v, ponto_c)
        self.play(
            self.camera.frame.animate.move_to(pontos_importantes.get_center()).set(width=grade.x_length * 1.1),
            run_time=2
        )
        self.wait(3)

        
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width),
            run_time=1.5
        )