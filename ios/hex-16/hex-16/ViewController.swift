//
//  ViewController.swift
//  hex-16
//
//  Created by Bimo on 2020-03-28.
//  Copyright © 2020 carleotn. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var hexText: UITextField!
    @IBOutlet weak var encodeButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.destination is EncodeViewController {
            let viewController = segue.destination as? EncodeViewController
            viewController?.hexcode = hexText.text
        }
    }
}

