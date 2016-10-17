from lettuce import step, world
from figura import Figuras


@step(u'dado que tengo el lado del cuadrado "([^"]*)"')
def dado_que_tengo_el_lado_del_cuadrado_group1(step, lado):
    world.figura = Figuras()
    world.lado_cuadratico = float(lado)


@step(u'cuando realizo el calculo de area del cuadrado')
def cuando_realizo_el_calculo_de_area_del_cuadrado(step):
    world.area = world.figura.cuadrado(world.lado_cuadratico)


@step(u'entonces obtengo el area "([^"]*)"')
def entonces_obtengo_el_area_group1(step, area_esperada):
    assert world.area == float(area_esperada), \
        'El area no es igual al esperado, area = ' + \
        world.area + 'area esperada = ' + area_esperada


@step(u'dado que tengo la base y altura de un rectangulo "([^"]*)" "([^"]*)"')
def dado_que_tengo_la_base_y_la_altura_de_un_rectangulo(step, altura, base):
    world.figura = Figuras()
    world.base_figura = float(base)
    world.altura_figura = float(altura)


@step(u'cuando realizo el calculo de area del rectangulo')
def cuando_realizo_el_calculo_de_area_del_rectangulo(step):
    world.area = world.figura.rectangulo(
        world.base_figura, world.altura_figura)


@step(u'dado que tengo la base y la altura de' +
      ' un triangulo "([^"]*)" "([^"]*)"')
def dado_que_tengo_la_base_y_la_altura_de_un_triangulo(step, base, altura):
    world.figura = Figuras()
    world.base_figura = float(base)
    world.altura_figura = float(altura)


@step(u'cuando realizo el calculo del area del triangulo')
def cuando_realizo_el_calculo_del_area_del_triangulo(step):
    world.area = world.figura.triangulo(world.base_figura, world.altura_figura)


@step(u'dado que tengo el radio "([^"]*)"')
def dado_que_tengo_el_radio_group1(step, radio):
    world.figura = Figuras()
    world.radio_figura = float(radio)


@step(u'cuando realizo el calculo de area de la circuanferencia')
def cuando_realizo_el_calculo_de_area_de_la_circuanferencia(step):
    world.area = world.figura.circunferencia(world.radio_figura)
