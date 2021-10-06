from physics.delta_t_calculators import DefaultDeltaTCalculator, FixedDeltaTCalculator


def test_default_dt_calculator(mocker):
    import time

    fake_timer = [10, 10, 15, 18]
    mocker.patch.object(time, "time", new=lambda *args, **kwargs: fake_timer.pop(0))
    dt_calculator = DefaultDeltaTCalculator()
    assert dt_calculator() == 5
    assert dt_calculator() == 3


def test_(mocker):
    some_dt = 1.1
    dt_calculator = FixedDeltaTCalculator(delta_t=some_dt)
    assert dt_calculator() == some_dt
    assert dt_calculator() == some_dt
