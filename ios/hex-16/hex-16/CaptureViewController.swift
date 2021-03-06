//
//  CaptureViewController.swift
//  hex-16
//
//  Created by Bimo on 2020-04-02.
//  Copyright © 2020 carleotn. All rights reserved.
//

import UIKit

class CaptureViewController: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {

    @IBOutlet weak var imageView: UIImageView!
    
    @IBAction func takePhotoButton(_ sender: UIButton) {
        imagePicker =  UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.sourceType = .camera

        present(imagePicker, animated: true, completion: nil)
    }
    
    @IBAction func decodePhotoButton(_ sender: UIButton) {
    }
    
    var imagePicker: UIImagePickerController!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    // MARK: - Image Picker
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        imagePicker.dismiss(animated: true, completion: nil)
        imageView.image = info[.originalImage] as? UIImage
        
        UIImageWriteToSavedPhotosAlbum(imageView.image!, nil, nil, nil);
    }
    
    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.destination is DecodeViewController, imageView.image != nil {
            let viewController = segue.destination as? DecodeViewController
            viewController?.hexImage = imageView.image
        }
    }
}
