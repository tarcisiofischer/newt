#===================================================================================================
# ForceGenerator
#===================================================================================================
class ForceGenerator(object):

    def update(self, obj):
        '''
        Updates the object, applying the current force to it.

        :param object obj:
            Object where the force will be applied to

        :returns np.array(shape=(3,), dtype=np.float64):
            The generated force vector
        '''
