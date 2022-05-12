from durable.lang import *

with ruleset('Machine'):
    @when_all((m.predicate == '안켜진다') & (m.object == '전원이'))
    def check1(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '확인한다', 'object': '전원코드를' })
		
    @when_all((m.predicate == '안켜진다') & (m.object == '전원이'))
    def check2(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '확인한다', 'object': '파워서플라이를' })

    @when_all((m.predicate == '안된다') & (m.object == '통신이'))
    def check3(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '확인한다', 'object': 'Cable을' })

    @when_all((m.predicate == '안된다') & (m.object == '통신이'))
    def check4(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '확인한다', 'object': 'Port의 LED를' })

    @when_all((m.predicate == '안된다') & (m.object == '통신이'))
    def check5(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '확인한다', 'object': 'IP를' })

    @when_all((m.predicate == '안된다') & (m.object == '통신이'))
    def check6(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '해본다', 'object': 'Ping테스트를' })

    @when_all((m.predicate == '안된다') & (m.object == '입력이'))
    def check7(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '재연결해본다', 'object': '입력장치를' })

    @when_all((m.predicate == '안된다') & (m.object == '입력이'))
    def check8(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '해본다', 'object': '원격접속을' })
		
    @when_all((m.predicate == '안된다') & (m.object == '입력이'))
    def check9(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '재기동한다', 'object': '강제로' })

    @when_all((m.predicate == '느리다') & (m.object == '속도가'))
    def check10(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '체크한다', 'object': 'Process를' })

    @when_all((m.predicate == '느리다') & (m.object == '속도가'))
    def check11(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'Kill한다', 'object': '사용량이 많은 Process를' })

    @when_all((m.predicate == '느리다') & (m.object == '속도가'))
    def check12(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '재기동한다', 'object': '데몬을' })

    @when_all((m.predicate == '안된다') & (m.object == '부팅이'))
    def check13(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '확인한다', 'object': 'DISK의 LED를' })

    @when_all((m.predicate == '안된다') & (m.object == '부팅이'))
    def check14(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '해본다', 'object': 'Single 부팅을' })
		
    @when_all((m.predicate == '안된다') & (m.object == '부팅이'))
    def check15(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '복구한다', 'object': 'Backup본으로' })
		
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.object, c.m.predicate, ))


assert_fact('Machine', { 'subject': 'Server', 'object': '입력이', 'predicate': '안된다' })
assert_fact('Machine', { 'subject': 'Service', 'object': '속도가', 'predicate': '느리다' })
assert_fact('Machine', { 'subject': 'Server', 'object': '전원이', 'predicate': '안켜진다' })
assert_fact('Machine', { 'subject': 'OS', 'object': '부팅이', 'predicate': '안된다' })
assert_fact('Machine', { 'subject': 'Server', 'object': '통신이', 'predicate': '안된다' })  
