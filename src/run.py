####################################################################################################
## Script Details                                                                                 ##
####################################################################################################
#                                                                                                 ##
# Project         : Flask Market place                                                            ##
# Author          : Varun Pius Rodrigues                                                          ##
# Description     : This is the implementation of the  online market web application              ##
#                                                                                                 ##
####################################################################################################
# Change Log:                                                                                     ##
# Date        Author                Description                                                   ##
####################################################################################################
#                                                                                                 ##
# 2022-07-18  Varun Pius Rodrigues  v1: Base application with basic folder structure              ##
# 2022-07-19  Varun Pius Rodrigues  v2: Folder structure setup                                    ##
# 2022-07-19  Varun Pius Rodrigues  v3: User Model with Login and Registration page               ##
# 2022-07-19  Varun Pius Rodrigues  v4: User Authentication                                       ##
# 2022-07-19  Varun Pius Rodrigues  v5: Item buying and selling                                   ##
####################################################################################################
# TODO:                                                                                           ##
#   - Use FLASK_DEBUG instead of FLASK_ENV as FLASK_ENV is deprecated                             ##
#   - Create profile page, with ability to add money to wallet
#   - Notes on hidden_tag() for csrf 
#   - Test with multiple Docker web and single db containers
#   - Session mgmt: 
#       - include timeout
#       - JWT
####################################################################################################
# - .dockerignore
# - https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef
# - CHECK: https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa
#          https://www.stefanproell.at/tags/docker-compose.-grant/
####################################################################################################


from market import app

if __name__ == '__main__':
    app.run(debug=True)
