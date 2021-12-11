import casefoam

baseCase = 'HFP'
caseStructure = [['angle_02', 'angle_03', 'angle_04'],
                 ['grid1', 'grid2' ]]

# update_grid1 = {
#    'system/blockMeshDict': {'#!stringManipulation': {'varA': '23',
#                                                      'varB': '8',
#                                                      'varC': '19',
#                                                      'varD': '42',
#                                                      'varE': '4'}},
# }

# update_grid2 = {
#    'system/blockMeshDict': {'#!stringManipulation': {'varA': '46',
#                                                      'varB': '16',
#                                                      'varC': '38',
#                                                      'varD': '84',
#                                                      'varE': '8'}},
# }

# update_grid3 = {
#    'system/blockMeshDict': {'#!stringManipulation': {'varA': '69',
#                                                      'varB': '24',
#                                                      'varC': '57',
#                                                      'varD': '126',
#                                                      'varE': '12'}},
# }


def update_grid(x1, x2, x3, x4, y1, y2):
    return {
        'system/blockMeshDict': {'#!stringManipulation': {'varX1': '%s' % x1,
                                                          'varX2': '%s' % x2,
                                                          'varX3': '%s' % x3,
                                                          'varX4': '%s' % x4,
                                                          'varY1': '%s' % y1,
                                                          'varY2': '%s' % y2}}
    }


def update_angle(angle):
    return {
        'system/blockMeshDict': {'#!stringManipulation':
                                 {'var_angle': '%s' % angle}}
    }


caseData = {
    'angle_02': update_angle(4.24977),
    'angle_03': update_angle(6.02654),
    'angle_04': update_angle(7.85898),
    'grid1': update_grid(200, 40, 120, 60, 200, 10),
    'grid2': update_grid(200*2, 40*2, 120*2, 60*2, 200*2, 10*2),
   #'grid3': update_grid(200*3, 40*3, 120*3, 60*3, 200*3, 10*3)
}

# generate cases
casefoam.mkCases(baseCase, caseStructure, caseData, hierarchy='tree',
                 writeDir='Cases')
