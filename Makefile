PY = python

solve:
	${PY} von-bertanlanffy-solve.py

draw:
	${PY} draw_von.py

distribution:
	${PY} distribution.py

eat:
	${PY} eat.py

clean:
	rm ./figures/* -rf