Basically, this is something that you never ever use. However, there are rare
cases where it might be fun to use anyway. Here's how you can use it for
implementing some weapons for a very simple game:

    from states import StatefulObject
    import time
    
    class Reloading(object):
        @staticmethod
        def reload(self):
            pass
    
        @staticmethod
        def fire(self):
            if time.time() > self.reload_start_time:
                self.popState()
                self.fire()
    
            print 'Can not fire while reloading.'
    
    class Empty(object):
        @staticmethod
        def reload(self):
            print('No ammo to load!')
    
        @staticmethod
        def fire(self):
            if self.ammo_remaining > 0:
                self.popState()
                self.fire()
            else:
                print('Can not fire while out of ammo.')
    
    class Weapon(StatefulObject):
        damage = 20
        ammo_remaining = 75
        ammo_in_clip = 25
    
        reload_time = 500
    
        auto_reload = True
        reload_class = Reloading
        empty_class = Empty
    
        def reload(self):
            self.reload_start_time = time.time()
            self.pushState(self.reload_class)
    
        def fire(self):
            print('Firing {0} for {1} damage.'.format(self.__class__.__name__, self.damage)
    
            self.ammo_remaining -= 1
            self.ammo_in_clip -= 1
    
            if self.ammo_remaining == 0:
                self.pushState(self.empty_class)
    
            elif self.ammo_remaining == 0 and self.auto_reload:
                self.reload()
    
    class RocketLauncher(Weapon):
        damage = 100
    
        ammo_remaining = 15
        ammo_in_clip = 2
    
        reload_time = 1800
    
