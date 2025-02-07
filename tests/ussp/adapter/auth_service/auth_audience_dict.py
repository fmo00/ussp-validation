from constant.authentication import AuthenticationConstant 

#TODO: use import for better readability and cleaner dict

audience_dictionary = {
    AuthenticationConstant.USSP_CLIENT_TYPE: AuthenticationConstant.INTENDED_AUDIENCE_USSP_VALUE,
    AuthenticationConstant.DSS_CLIENT_TYPE: AuthenticationConstant.INTENDED_AUDIENCE_DSS_VALUE,
}