import argparse

REPLACEABLE = "alou_%s_voce"


class EndpointReplaceUrlAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        new_val = REPLACEABLE % values
        setattr(namespace, self.dest, new_val)

parser = argparse.ArgumentParser()
parser.add_argument('--eureka', action=EndpointReplaceUrlAction)

args = parser.parse_args('--eureka FFFFFF'.split())

print("eureka_p", args.eureka)

