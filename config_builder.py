#!/usr/bin/env python


# --- imports
import argparse
import sys
lib_path = "lib"
sys.path.append(lib_path)
import common



# --- env vars

usecase_file = "topology/usecase.json"


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-lu', '--list_usecase', help='List usecases', action='store_true')
    parser.add_argument('-ln', '--list_nid', help='List available NIDs', required=False)
    parser.add_argument('-u', '--usecase', help='Usecase to be provisioned', required=False)
    parser.add_argument('-n', '--nid', help='NID to be provisioned', required=False)
    args = parser.parse_args()

    usage = "ERROR!!\nUsage: config_builder.py --usecase \"Usecase name\" --nid \"NID\""
    usage2 = "Verify: config_builder.py --list_nid \"usecase\""
    usage3 = "Verify: config_builder.py --list_usecase"

    gusecase = common.read_usecase(usecase_file)
    usecase = common.get_dict(gusecase, 0)

    if args.list_usecase:
        common.list_keys(usecase)
        print usecase['Inter_State_EVC_EREACH_Over_ACCESS_EPL']['vendor'].keys()
        exit()
    elif args.list_nid:
        if args.list_nid in usecase:
            common.list_keys(usecase[args.list_nid]['vendor'])
        else:
            print "ERROR!! usecase not found\n" + usage3
        exit()
    elif args.nid and args.usecase:
        if args.usecase in usecase:
            if args.nid in usecase[args.usecase]['vendor']:
                print "Success"
                common.provision_usecase(usecase, args.usecase, args.nid)
            else:
                print "ERROR: Nid not found\n" + usage2
                exit()
        else:
            print "ERROR: Usecase not found\n" + usage3

    else:
        print usage
        exit()


