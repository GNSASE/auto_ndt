from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings  # import the settings file


#Setup shared logging handler
import logging
from shared_common.shared_logger import initialize_logger
initialize_logger(settings.LOGGING_PATH)  # path in django settings file

#Import database methods
import shared_common.shared_db as database

#Import xml functions
from shared_common.shared_xml import xml_read_variables

###!!!!!!!!!!!!!!!!!
## This view is the main entry point into the webgui
###!!!!!!!!!!!!!!!!!


@csrf_exempt
def ndt_index(request):
    # Query the database for a list of scale units stored.
    scale_units = database.fetch_scale_unit()
    return render(request, 'ndt_frontpage.html', {'scale_units': scale_units})


###!!!!!!!!!!!!!!!!!
## This view accepts the submit input form from the main entry point
## of view above if the user has submitted a new NDT.
###!!!!!!!!!!!!!!!!!
@csrf_exempt
def ndt_new(request):
    logging.debug("New incoming ndt_new request: {}".format(request.POST))
    if not request.POST:
        return HttpResponse("""Your request could not be recognized.
                               Please try again.""")

    try:
        db_results = database.search_ndt(request.POST['pid_number'])

        if db_results:
            """
            Return to the user that the pid_number already exists and
            render the existing and render to the user the edit/view
            page with all pid data.
            !!! THIS EVALUATES WHETHER OR NOT THE PID ALREADY EXISTS !!!
            """
            logging.debug("""The PID number already exists for this
                             request, we should now display the
                             view/edit page.""")
            try:
                """
                db_results[1] is the scale_unit value stored from
                the db query for the existing PID.
                """
                if request.POST['pid_number'] and db_results[1]:
                    """
                    Using the pid number and scale_unit we will
                    attempt to create a filename and replace the
                    template variables with the users input from
                    the submitted form.
                    """
                    # First we need to read in the xml template file
                    filename = database.fetch_xml_template(db_results[1])
                    xml_variables = xml_read_variables("Variables",
                                                       '{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                                        filename[0]))

            except Exception as e:
                logging.error('{}'.format(e))
                return render(request, 'error.html',
                              {'error_text': """An error occured while
                              loading the variable xml files.  Please
                              report this issue to garyw@microsoft.com"""})


            try:
                """
                Query database for all newly inserted data for the
                form variables and return the results.
                """
                stored_variable_data = database.fetch_ndt_form_data(request.POST['pid_number'])

            except Exception as e:
                logging.error('{}'.format(e))
                return render(request, 'error.html',
                              {'error_text': """An error occured
                              fetching the newly stored user data for
                              this PID from the database.
                              Please report this issue to
                              garyw@microsoft.com"""})

            try:
                """
                Now that new XML data has been written,
                load the xml file to display interface info.
                """
                xml_interfaces = xml_read_variables("Interfaces",
                                                    '{}/{}'.format(settings.USER_CREATED_XML_PATH,
                                                    request.POST['pid_number']+'_'+filename[0]))

            except Exception as e:
                logging.error('{}'.format(e))
                message = HttpResponse()
                message.write("""An error occured while loading new values
                              from saved xml for this PID.
                              Please report this issue to
                              garyw@microsoft.com""")
                return message


            return render(request, 'ndt_edit.html',
                          {'query_dict_iter': request.POST.iterlists(),
                           'query_dict': request.POST,
                           'filename': '{}_{}'.format(request.POST['pid_number'],filename[0]),
                           'xml_variables': xml_variables,
                           'db_results': stored_variable_data,
                           'xml_interfaces': xml_interfaces})



    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write("""An error occured while querying the database.
                      Please report this issue to garyw@microsoft.com""")
        return message

    try:

        """
        This will execute an xml load function to fetch the
        Variables section of the selected scale unit to return to the
        web form to build the gui web form template index.

        Execute a database call to retrieve the xml template
        variables and base network url for the selected scale_unit.
        """

        filename = database.fetch_xml_template(request.POST['scale_unit'])
        base_standard_url = database.fetch_base_standard_url(request.POST['scale_unit'])

        xml_variables = xml_read_variables("Variables",
                                           '{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                           filename[0]))

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write("""An error occured while attempting to load the
                      xml toplogy file.  Please report this issue to
                      garyw@microsoft.com""")
        return message

    # Return the results to rendering template.
    return render(request, 'ndt_new.html',
                  {'pid_number': request.POST['pid_number'],
                   'xml_variables': xml_variables,
                   'base_standard_url': base_standard_url[0],
                   'scale_unit': request.POST['scale_unit']})

###!!!!!!!!!!!!!!!!!
## This view accepts the submit input form from the new NDT submission variable assignment questionaire.
###!!!!!!!!!!!!!!!!!
@csrf_exempt
def ndt_new_submit(request):
    logging.debug("New incoming ndt_new_submit: {}".format(request.POST))
    if not request.POST:
        return HttpResponse("""Your request could not be recognized.
                              Please try again.""")

    try:

        if database.search_ndt(request.POST['pid_number']):
            """
            Return to the user that the pid_number already exists and render the existing
            and render to the user the edit/view page with all pid data.
            !!! THIS EVALUATES WHETHER OR NOT THE PID ALREADY EXISTS !!!
            """
            logging.debug("The PID number already exists for this request, we should now display the view/edit page.")
            message = HttpResponse("PID number already exists... need more content here...")
            return message

        else:
            database.create_ndt(request.POST['pid_number'],
                                request.POST['scale_unit'])

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while querying the database.  Please report this issue to garyw@microsoft.com')
        return message

    try:

        if request.POST['pid_number'] and request.POST['scale_unit']:
            """
            Using the pid number and scale_unit we will attempt to create a filename and replace the
            template variables with the users input from the submitted form.
            """
            # First we need to read in the xml template file
            filename = database.fetch_xml_template(request.POST['scale_unit'])
            xml_open = open('{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                           filename[0]),
                                           'r')
            xml_template = xml_open.read()
            xml_variables = xml_read_variables("Variables",
                                               '{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                               filename[0]))

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while loading the variable xml files.  Please report this issue to garyw@microsoft.com')
        return message

    try:
        """
        Create new xml file for the new NDT performing the variable substitution with the form values provided.
        !!! THIS CREATES THE NEW XML FILE WITH FORM SUBMITTED VALUES TEMPLATE SUBSTITUTIONS !!!
        """
        new_ndt_xml = open('{}/{}_{}'.format(settings.USER_CREATED_XML_PATH,
                                             request.POST['pid_number'],
                                             filename[0]),
                                             'w')

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while creating the new xml files for this PID.  Please report this issue to garyw@microsoft.com')
        return message

    try:
        """Iterate through the form submission and replace the template
        values with the user submitted data."""
        # loop through keys and values
        for key, value in request.POST.iteritems():
            """Below will intercept key value, split with :, indicating key,
               that it is a variable and which tab the variable will populate
               in the edit tabs and insert into db."""
            if ':template_variable' in key:
                key_split = key.split(":")
                _key = key_split[0]
                if value == "":
                    logging.debug("Skipping update of Key:{} as its value provided is blank.".format(_key))
                    continue
                logging.debug("Key {} Value {}".format(_key,
                                                       value))
                xml_template = xml_template.replace('%'+_key+'%',
                                                    value)
                try:
                    database.insert_form_key_value(request.POST['pid_number'],
                                                   request.POST['scale_unit'],
                                                   _key,
                                                   str(value))

                except Exception as e:
                    logging.error('{}'.format(e))
                    message = HttpResponse()
                    message.write('An error occured while inserting the key/value pair into the database.  Please report this issue to garyw@microsoft.com')
                    return message

        # Write the final results to a new xml file.
        new_ndt_xml.write(xml_template)
        new_ndt_xml.close()

        try:
            # Query database for all newly inserted data for the form variables and return the results.
            stored_variable_data = database.fetch_ndt_form_data(request.POST['pid_number'])

        except Exception as e:
            logging.error('{}'.format(e))
            message = HttpResponse()
            message.write('An error occured fetching the newly stored user data for this PID from the database.  Please report this issue to garyw@microsoft.com')
            return message

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured substituting user input with template variables in the new xml files for this PID.  Please report this issue to garyw@microsoft.com')
        return message

    try:
        # Now that new XML data has been written, load the xml file to display interface info
        xml_interfaces = xml_read_variables("Interfaces",
                                            '{}/{}'.format(settings.USER_CREATED_XML_PATH,
                                            request.POST['pid_number']+'_'+filename[0]))

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while loading new values from saved xml for this PID.  Please report this issue to garyw@microsoft.com')
        return message

    return render(request, 'ndt_edit.html', {'query_dict_iter': request.POST.iterlists(),
                                             'query_dict': request.POST,
                                             'filename': '{}_{}'.format(request.POST['pid_number'],
                                             filename[0]),
                                             'xml_variables': xml_variables,
                                             'db_results': stored_variable_data,
                                             'pid_number': request.POST['pid_number'],
                                             'scale_unit': request.POST['scale_unit'],
                                             'xml_interfaces': xml_interfaces})

###!!!!!!!!!!!!!!!!!
## This view accepts the submit input form from the main entry point edit tab or will accept redirect
## if the user attempts to create a new PID when the PID already exists in the database.
###!!!!!!!!!!!!!!!!!
@csrf_exempt
def ndt_edit_submit(request):
    logging.debug("New incoming ndt_edit request: {}".format(request.POST))
    if not request.POST:
        return HttpResponse("Your request could not be recognized.  Please try again.")


    try:
        db_results = database.search_ndt(request.POST['pid_number'])
        if db_results:
            """
            Using the pid number and scale_unit we will attempt to create a filename and replace the
            template variables with the users input from the submitted form.
            """
            # First we need to read in the xml template file
            filename = database.fetch_xml_template(db_results[1])
            xml_open = open('{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                           filename[0]),
                                           'r')
            xml_template = xml_open.read()
            xml_variables = xml_read_variables("Variables",
                                               '{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                               filename[0]))
            xml_interfaces = xml_read_variables("Interfaces",
                                                '{}/{}'.format(settings.USER_CREATED_XML_PATH,
                                                request.POST['pid_number']+'_'+filename[0]))

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while loading the variable xml files.  Please report this issue to garyw@microsoft.com')
        return message

    try:
        """
        Create new xml file for the new NDT performing the variable substitution with the form values provided.
        !!! THIS CREATES THE NEW XML FILE WITH FORM SUBMITTED VALUES TEMPLATE SUBSTITUTIONS !!!
        """
        new_ndt_xml = open('{}/{}_{}'.format(settings.USER_CREATED_XML_PATH,
                                             request.POST['pid_number'],
                                             filename[0]),
                                             'w')

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while creating the new xml files for this PID.  Please report this issue to garyw@microsoft.com')
        return message

    try:
        """Iterate through the form submission and replace the template values with the user submitted data."""
        # loop through keys and values
        for key, value in request.POST.iteritems():
            """Below will intercept key value, split with :, indicating key,
               that it is a variable and which tab the variable will populate
               in the edit tabs and insert into db."""
            if ':template_variable' in key:
                key_split = key.split(":")
                _key = key_split[0]
                if value == "":
                    logging.debug("Skipping update of Key:{} as its value provided is blank.".format(_key))
                    continue
                logging.debug("Key {} Value {}".format(_key,value))
                xml_template = xml_template.replace('%'+_key+'%',
                                                    value)
                try:
                    database.insert_form_key_value(request.POST['pid_number'],
                                                   db_results[1], _key,
                                                   str(value))

                except Exception as e:
                    logging.error('{}'.format(e))
                    message = HttpResponse()
                    message.write('An error occured while inserting the key/value pair into the database.  Please report this issue to garyw@microsoft.com')
                    return message

        # Write the final results to a new xml file.
        new_ndt_xml.write(xml_template)
        new_ndt_xml.close()

        try:
            # Query database for all newly inserted data for the form variables and return the results.
            stored_variable_data = database.fetch_ndt_form_data(request.POST['pid_number'])

        except Exception as e:
            logging.error('{}'.format(e))
            message = HttpResponse()
            message.write('An error occured fetching the newly stored user data for this PID from the database.  Please report this issue to garyw@microsoft.com')
            return message

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured substituting user input with template variables in the new xml files for this PID.  Please report this issue to garyw@microsoft.com')
        return message

    try:
        # Now that new XML data has been written, load the xml file to display interface info
        xml_interfaces = xml_read_variables("Interfaces",
                                            '{}/{}'.format(settings.USER_CREATED_XML_PATH,
                                            request.POST['pid_number']+'_'+filename[0]))

    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while loading new values from saved xml for this PID.  Please report this issue to garyw@microsoft.com')
        return message

    return render(request, 'ndt_edit.html', {'query_dict_iter': request.POST.iterlists(),
                                             'query_dict': request.POST,
                                             'filename': '{}_{}'.format(request.POST['pid_number'],
                                             filename[0]),
                                             'xml_variables': xml_variables,
                                             'db_results': stored_variable_data,
                                             'xml_interfaces': xml_interfaces})


###!!!!!!!!!!!!!!!!!
## This view accepts the submit input request edit a PID / NDT from the system if one exists.
###!!!!!!!!!!!!!!!!!
@csrf_exempt
def ndt_edit(request):
    logging.debug("New incoming ndt_edit request: {}".format(request.POST))
    if not request.POST:
        return render(request,
                      'error.html',
                      {'error_text': "Your request could not be recognized.  Please try again."})

    try:
        if request.POST['pid_number']:
            db_results = database.search_ndt(request.POST['pid_number'])

            if db_results:
                """
                Return to the user that the pid_number already exists and render the existing
                and render to the user the edit/view page with all pid data.
                !!! THIS EVALUATES WHETHER OR NOT THE PID ALREADY EXISTS !!!
                """
                logging.debug("The PID number already exists for this request, we should now display the view/edit page.")
                pass

            else:
                logging.debug("The PID number _DOES_NOT_ already exist for this request, Please go back and create a new NDT for this PID.")
                return render(request,
                              'error.html',
                              {'error_text': "The PID number _DOES_NOT_ already exist for this request, Please go back and create a new NDT for this PID."})

        else:
            logging.debug("Please provide a valid PID number for this request, Please go back and create a new NDT for this PID.")
            return render(request,
                          'error.html',
                          {'error_text': "Please provide a valid PID number for this request, Please go back and create a new NDT for this PID."})


    except Exception as e:
        logging.error('{}'.format(e))
        return render(request,
                      'error.html',
                      {'error_text': "An error occured looking up the PID in the database.  Please report this issue to garyw@microsoft.com"})

    try:
        """db_results[1] is the scale_unit value stored from the db query for the existing PID."""
        if request.POST['pid_number'] and db_results[1]:
            """
            Using the pid number and scale_unit we will attempt to create a filename and replace the
            template variables with the users input from the submitted form.
            """
            # First we need to read in the xml template file
            filename = database.fetch_xml_template(db_results[1])
            xml_variables = xml_read_variables("Variables",
                                               '{}/{}'.format(settings.XML_TOPOLOGY_PATH,
                                               filename[0]))
            xml_interfaces = xml_read_variables("Interfaces",
                                                '{}/{}'.format(settings.USER_CREATED_XML_PATH,
                                                request.POST['pid_number']+'_'+filename[0]))


    except Exception as e:
        logging.error('{}'.format(e))
        return render(request,
                      'error.html',
                      {'error_text': "An error occured while loading the variable xml files.  Please report this issue to garyw@microsoft.com"})


    try:
        # Query database for all newly inserted data for the form variables and return the results.
        stored_variable_data = database.fetch_ndt_form_data(request.POST['pid_number'])

    except Exception as e:
        logging.error('{}'.format(e))
        return render(request,
                      'error.html',
                      {'error_text': "An error occured fetching the newly stored user data for this PID from the database.  Please report this issue to garyw@microsoft.com"})



    return render(request, 'ndt_edit.html', {'query_dict_iter': request.POST.iterlists(),
                                             'query_dict': request.POST,
                                             'filename': '{}_{}'.format(request.POST['pid_number'],
                                             filename[0]),
                                             'xml_variables': xml_variables,
                                             'db_results': stored_variable_data,
                                             'xml_interfaces': xml_interfaces})

###!!!!!!!!!!!!!!!!!
## This view accepts the submit input request to delete a PID / NDT from the system if one exists.
###!!!!!!!!!!!!!!!!!
@csrf_exempt
def ndt_delete(request):
    logging.debug("New ndt_delete request: {}".format(request.POST))
    if not request.POST:
        return HttpResponse("Your request could not be recognized.  Please try again.")

    try:
        """
        The user has requested that the PID entry be deleted so the function call below
        will remove the PID number matching row in ndt_index table.
        """
        database.delete_ndt(request.POST['pid_number'])


    except Exception as e:
        logging.error('{}'.format(e))
        message = HttpResponse()
        message.write('An error occured while querying the database.  Please report this issue to garyw@microsoft.com')
        return message

    return render(request, 'ndt_removed.html',
                  {'pid_number': request.POST['pid_number']})