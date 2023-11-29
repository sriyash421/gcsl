# import doodad as dd
# import gcsl.doodad_utils as dd_utils

def run(output_dir='/tmp', env_name='pointmass_empty', gpu=True, seed=0, **kwargs):

    import gym
    import numpy as np
    from rlutil.logging import log_utils, logger

    import rlutil.torch as torch
    import rlutil.torch.pytorch_util as ptu

    # Envs

    from gcsl import envs
    from gcsl.envs.env_utils import DiscretizedActionEnv

    # Algo
    from gcsl.algo import buffer, gcsl, variants, networks

    ptu.set_gpu(0)
    if not gpu:
        print('Not using GPU. Will be slow.')

    torch.manual_seed(seed)
    np.random.seed(seed)

    env = envs.create_env(env_name)
    # env.render()
    env_params = envs.get_env_params(env_name)
    print(env_params)

    env, policy, replay_buffer, gcsl_kwargs = variants.get_params(env, env_params)
    algo = gcsl.GCSL(
        env,
        policy,
        replay_buffer,
        **gcsl_kwargs
    )

    exp_prefix = 'example/%s/gcsl/' % (env_name,)

    with log_utils.setup_logger(exp_prefix=exp_prefix, log_base_dir=output_dir):
        algo.train()


if __name__ == "__main__":
    params = {
        'seed': 0,
        'env_name': 'pointmass_rooms', #['lunar', 'pointmass_empty','pointmass_rooms', 'pusher', 'claw', 'door'],
        'gpu': True,
        'output_dir': './results4/gcsl_hitl'
    }
    run(**params)
    # dd_utils.launch(run, params, mode='local', instance_type='c4.xlarge')
