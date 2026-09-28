from manim import *
import numpy as np

class plano(MovingCameraScene):
    def construct(self):
        # 1 Configuração de Fundo e Logo
        cordefundo = ManimColor("#D5D5DD")
        self.camera.background_color = cordefundo

        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff=0.1)
            self.add(img)
        except:
            print('LOGO NAO ENCONTRADA')

        
        titulo = Tex(r"Plano Cartesiano: Fundamentos", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))

        # 3 Construção dos Eixos
        reta_X = NumberLine(x_range=[-10, 10], color=BLACK, stroke_width=2)
        reta_Y = NumberLine(x_range=[-10, 10], color=BLACK, stroke_width=2)
        
        self.play(Create(reta_X), Create(reta_Y))
        self.play(reta_Y.animate.rotate(90 * DEGREES, about_point=ORIGIN))
        
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
        self.play(FadeIn(grade))
        self.wait()

        # 4 Conceito de Unidade 
        # Mostra que o plano é feito de quadrados de 1x1
        unidade_box = Square(side_length=1, color=BLUE, fill_opacity=0.3).move_to([0.5, 0.5, 0])
        texto_unidade = Text("1 Unidade", color=BLUE, font_size=20).next_to(unidade_box, UP+RIGHT, buff=0.1)
        
        self.play(self.camera.frame.animate.scale(0.4).move_to([0.5, 0.5, 0]))
        self.play(Create(unidade_box), Write(texto_unidade))
        self.wait()
        self.play(FadeOut(unidade_box, texto_unidade), self.camera.frame.animate.scale(1/0.4).move_to(ORIGIN))

        # 5 Quadrantes e Sinais
        quadrantes = VGroup(
            Polygon(ORIGIN, RIGHT*12, RIGHT*12+UP*12, UP*12, fill_color=PURE_GREEN, fill_opacity=0.15, stroke_width=0),
            Polygon(ORIGIN, LEFT*12, LEFT*12+UP*12, UP*12, fill_color=PURE_RED, fill_opacity=0.15, stroke_width=0),
            Polygon(ORIGIN, LEFT*12, LEFT*12+DOWN*12, DOWN*12, fill_color=YELLOW, fill_opacity=0.15, stroke_width=0),
            Polygon(ORIGIN, RIGHT*12, RIGHT*12+DOWN*12, DOWN*12, fill_color=PINK, fill_opacity=0.15, stroke_width=0)
        )
        
        sinais = VGroup(
            MathTex("(+, +)", color=BLACK).move_to([3, 2, 0]),
            MathTex("(-, +)", color=BLACK).move_to([-3, 2, 0]),
            MathTex("(-, -)", color=BLACK).move_to([-3, -2, 0]),
            MathTex("(+, -)", color=BLACK).move_to([3, -2, 0])
        )

        self.play(FadeIn(quadrantes), Write(sinais))
        self.wait(2)
        self.play(FadeOut(quadrantes), FadeOut(sinais))

        # 6 Pontos Estáticos (Projeções em X e Y)
        def criar_ponto(coord, cor, tex):
            p = Dot(coord, color=cor, radius=0.08)
            l = MathTex(tex, color=BLACK).scale(0.8).next_to(p, UR, buff=0.1)
           
            lv = DashedLine(start=[coord[0], 0, 0], end=coord, color=GRAY, stroke_width=2)
            lh = DashedLine(start=[0, coord[1], 0], end=coord, color=GRAY, stroke_width=2)
            return VGroup(p, l, lv, lh)

        p1 = criar_ponto([3, 2, 0], PURE_RED, "(3, 2)")
        p2 = criar_ponto([-4, 3, 0], PURE_GREEN, "(-4, 3)")
        p3 = criar_ponto([-2, -3, 0], PURE_BLUE, "(-2, -3)")

        for p in [p1, p2, p3]:
            self.play(Create(p[2]), Create(p[3]))
            self.play(Create(p[0]), Write(p[1]))
        
        self.wait(2)
        self.play(FadeOut(p1, p2, p3))

        # 7 Pontos nos Eixos e Dinâmica
        ponto_movel = Dot([1, 1, 0], color=BLUE)
        
        # Redesenha a linha vertical (projeção no eixo X)
        h_line = always_redraw(lambda: 
            DashedLine(
                start=[ponto_movel.get_center()[0], 0, 0],
                end=ponto_movel.get_center(),
                color=GRAY, stroke_width=2
            ) if abs(ponto_movel.get_center()[1]) > 0.05 else VectorizedPoint(ponto_movel.get_center())
        )
        
        # Redesenha a linha horizontal (projeção no eixo Y)
        v_line = always_redraw(lambda: 
            DashedLine(
                start=[0, ponto_movel.get_center()[1], 0],
                end=ponto_movel.get_center(),
                color=GRAY, stroke_width=2
            ) if abs(ponto_movel.get_center()[0]) > 0.05 else VectorizedPoint(ponto_movel.get_center())
        )

        label_coords = always_redraw(lambda: 
            MathTex(
                f"({ponto_movel.get_center()[0]:.1f}, {ponto_movel.get_center()[1]:.1f})", 
                color=BLACK
            ).scale(0.7).next_to(ponto_movel, UR, buff=0.1)
        )

        texto_reforco = Text("Pontos sobre os eixos:", color=BLACK, font_size=30).to_corner(UP+LEFT)
        
        self.play(Write(texto_reforco))
        self.play(Create(ponto_movel))
        self.play(FadeIn(h_line), FadeIn(v_line), Write(label_coords))
        
       
        self.play(ponto_movel.animate.move_to([5, 0, 0]), run_time=2)
        self.play(Indicate(ponto_movel))
        self.wait()

        self.play(ponto_movel.animate.move_to([0, -3, 0]), run_time=2)
        self.play(Indicate(ponto_movel))
        self.wait(2)


        #apagar tudo
        self.play(FadeOut(ponto_movel), FadeOut(h_line), FadeOut(v_line), FadeOut(label_coords), FadeOut(texto_reforco))