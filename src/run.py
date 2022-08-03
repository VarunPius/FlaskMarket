####################################################################################################
## Script Details                                                                                 ##
####################################################################################################
#                                                                                                 ##
# Project         : Flask Market place                                                            ##
# Author          : Varun Pius Rodrigues                                                          ##
# Description     : This is the implementationof the  online market web application               ##
#                                                                                                 ##
####################################################################################################
# Change Log:                                                                                     ##
# Date        Author                Description                                                   ##
####################################################################################################
#                                                                                                 ##
# 2022-07-18  Varun Pius Rodrigues  v1: Base application with basic folder structure              ##
# 2022-07-19  Varun Pius Rodrigues  v2: Folder structure setup                                    ##
#                                                                                                 ##
####################################################################################################
# TODO:                                                                                           ##
#   - Use FLASK_DEBUG instead of FLASK_ENV as FLASK_ENV is deprecated                             ##
#   - Notes on hidden_tag() for csrf
####################################################################################################
# - .dockerignore
# - https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef
# - CHECK: https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa
#          https://www.stefanproell.at/tags/docker-compose.-grant/
####################################################################################################


from market import app

if __name__ == '__main__':
    app.run(debug=True)
