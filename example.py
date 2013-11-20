import pyrc
import pyrc.utils.hooks as hooks

class GangstaBot(pyrc.Bot):
  @hooks.command()
  def bling(self, target, sender):
    "will print yo"
    if misc.is_channel(target):
      self.message(target, "%s: yo" % sender)
    else:
      self.message(target, "yo")

  @hooks.command("^repeat\s+(?P<msg>.+)$")
  def repeat(self, target, sender, **kwargs):
    "will repeat whatever yo say"
    if misc.is_channel(target):
      self.message(target, kwargs["msg"])
    else:
      self.message(sender, kwargs["msg"])

  @hooks.privmsg("(lol|lmao|rofl(mao)?)")
  def stopword(self, target, sender, *args):
    """
    will repeat 'lol', 'lmao, 'rofl' or 'roflmao' when seen in a message
    only applies to channel messages
    """
    if misc.is_channel(target):
      self.message(target, args[0])

  @hooks.interval(10000)
  def keeprepeating(self):
    "will say something"
    self.message("#turntechgodhead", "stop repeating myself")

if __name__ == '__main__':
  bot = GangstaBot('irc.freenode.net', channels = ['#turntechgodhead'])
  bot.connect()
