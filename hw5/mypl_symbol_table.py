class SymbolTable(object):
    """A symbol table consists of a stack of environments, where each
    environment maps a (variable) name to its associated information
    """
    def __init__(self):
        self.scopes = [] # list of {id_name:info}
    
    def __environment(self, name):
        # search from last (most recent) to first environment
        for i in range(len(self.scopes)-1, -1, -1):
            if name in self.scopes[i]:
                return self.scopes[i]

    def id_exists(self, identifier):
        return self.__environment(identifier) != None
    
    def add_id(self, identifier):
        # can't add if no environments
        if not self.scopes:
            return
        # add to the most recently added environemt
        self.scopes[-1][identifier] = None
    
    def get_info(self, identifier):
        env = self.__environment(identifier)
        if env is not None:
            return env[identifier]
    
    def set_info(self, identifier, info):
        env = self.__environment(identifier)
        if env is not None:
            env[identifier] = info
    
    def push_environment(self):
        self.scopes.append({})
    
    def pop_environment(self):
        if len(self.scopes) > 0:
            self.scopes.pop()
    
    def __str__(self):
        return str(self.scopes)