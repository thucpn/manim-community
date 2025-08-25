docker run -it --name test -v "/Users/thucpn/Desktop/manim-community/example_scenes:/manim" manimcommunity/manim bash

manim -qm test.py PyramidVisualization
manim -qm math9.py AdvancedTriangleProblem
manim -qm math9_2.py TriangleConfiguration
manim -qm math9_3.py GeometryProblem


manim -pqh --resolution 1080,1920 math9_5.py MathProblemShort

manim -qm --resolution 1080,1920 math9_7_claude.py EulerLineProof