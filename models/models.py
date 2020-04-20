
def create_model(opt):
    model = None
    print(opt.model)
    if opt.model == 'IR2VI':
        assert(opt.dataset_mode == 'unaligned')
        from .ROI_focal_model import ROIFocalModel
        model = ROIFocalModel()
    elif opt.model == 'pix2pix':
        assert(opt.dataset_mode == 'aligned')
        from .pix2pix_model import Pix2PixModel
        model = Pix2PixModel()
    elif opt.model == 'test':
        assert(opt.dataset_mode == 'single')
        from .test_model import TestModel
        model = TestModel()
    else:
        raise ValueError("Model [%s] not recognized." % opt.model)
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))
    return model
