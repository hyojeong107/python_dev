from game.sound.echo import echo_test #=> 절대경로
#from ..sound.echo import echo_test # 상대경로 

def render_test():
    """ 
    render_test
    """
    print('테스트 vs code에서')
    echo_test()

render_test()