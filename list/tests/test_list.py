from algorithms.list import SinglyLinkedList

"""
To Run:
pytest -q test_graph.py
"""
class TestSinglyLinkedList:
    '''
    Test class
    '''
    def setup_class(self):
        '''
        setup
        '''
        pass

    def test_should_at_node_to_head(self):
        """ Adds not to head"""
        # arrange
        singly = SinglyLinkedList()

        # act
        singly.add(1)
        singly.add(2)
        singly.add(3)

        # assert
        agg_str = str(singly)
        assert agg_str == "1->2->3"
